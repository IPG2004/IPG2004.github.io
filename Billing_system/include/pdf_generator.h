// pdf_generator.h
#ifndef PDF_GENERATOR_H
#define PDF_GENERATOR_H

#include <cmath>
#include <string>
#include <vector>
#include <hpdf.h>
#include "utils.h"

// Clase para representar un producto en la factura
struct Product {
    std::string name;
    double price;
    int quantity;
};

// Clase para generar el PDF de la factura
class PDFGenerator {
public:
    PDFGenerator();  // Constructor
    ~PDFGenerator();  // Destructor

    bool createPDF(const std::string& filename, const std::string& clientName, const std::vector<Product>& products);
private:
    void addText(HPDF_Doc& pdf, const std::string& text, float x, float y, HPDF_Font font, float fontSize);
    void addProductTable(HPDF_Doc& pdf, const std::vector<Product>& products);
};

#endif
