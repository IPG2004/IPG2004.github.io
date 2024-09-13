// pdf_generator.cc
#include "pdf_generator.h"
#include <iostream>

// Constructor
PDFGenerator::PDFGenerator() {}

// Destructor
PDFGenerator::~PDFGenerator() {}

// Función para crear el PDF de la factura
bool PDFGenerator::createPDF(const std::string& filename, const std::string& clientName, const std::vector<Product>& products) {
    HPDF_Doc pdf = HPDF_New(nullptr, nullptr);
    if (!pdf) {
        std::cerr << "Error: Unable to create PDF object." << std::endl;
        return false;
    }

    HPDF_Font font = HPDF_GetFont(pdf, "Helvetica", nullptr);
    HPDF_Page page = HPDF_AddPage(pdf);

    HPDF_Page_SetSize(page, HPDF_PAGE_SIZE_A4, HPDF_PAGE_PORTRAIT);

    // Añadir título
    addText(pdf, "Invoice", 200, 800, font, 20);
    addText(pdf, "Client: " + clientName, 50, 750, font, 12);

    // Añadir tabla de productos
    addProductTable(pdf, products);

    // Guardar PDF
    try {
        HPDF_SaveToFile(pdf, filename.c_str());
    } catch (...) {
        std::cerr << "Error: Unable to save PDF file." << std::endl;
        HPDF_Free(pdf);
        return false;
    }

    HPDF_Free(pdf);
    return true;
}

// Función auxiliar para añadir texto al PDF
void PDFGenerator::addText(HPDF_Doc& pdf, const std::string& text, float x, float y, HPDF_Font font, float fontSize) {
    HPDF_Page page = HPDF_GetCurrentPage(pdf);
    HPDF_Page_BeginText(page);
    HPDF_Page_SetFontAndSize(page, font, fontSize);
    HPDF_Page_TextOut(page, x, y, text.c_str());
    HPDF_Page_EndText(page);
}

// Función para añadir la tabla de productos al PDF
void PDFGenerator::addProductTable(HPDF_Doc& pdf, const std::vector<Product>& products) {
    HPDF_Font font = HPDF_GetFont(pdf, "Helvetica", nullptr);
    HPDF_Page page = HPDF_GetCurrentPage(pdf);

    float x = 50;
    float y = 700;
    float lineHeight = 20;

    addText(pdf, "Product", x, y, font, 12);
    addText(pdf, "Price", x + 200, y, font, 12);
    addText(pdf, "Quantity", x + 300, y, font, 12);
    y -= lineHeight;

    for (const auto& product : products) {
        addText(pdf, product.name, x, y, font, 10);
        addText(pdf, doubleToStringWithTwoDecimals(product.price), x + 200, y, font, 10);
        addText(pdf, std::to_string(product.quantity), x + 300, y, font, 10);
        y -= lineHeight;
    }

    // Añadir total
    double total = 0.0;
    for (const auto& product : products) {
        total += product.price * product.quantity;
    }
    addText(pdf, "Total: $" + doubleToStringWithTwoDecimals(total), x, y - lineHeight, font, 12);
}
