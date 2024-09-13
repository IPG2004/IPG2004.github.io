// barcode_reader.cc
#include "barcode_reader.h"
#include <zbar.h>
#include <opencv2/opencv.hpp>
#include <iostream>

// Constructor
BarcodeReader::BarcodeReader() {}

// Destructor
BarcodeReader::~BarcodeReader() {}

// Función para preprocesar la imagen (convertirla a escala de grises y binarizarla)
cv::Mat BarcodeReader::preprocessImage(const cv::Mat& image) {
    cv::Mat gray, processed;
    // Convertir la imagen a escala de grises
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);
    // Binarizar la imagen usando un umbral adaptativo
    cv::threshold(gray, processed, 0, 255, cv::THRESH_BINARY | cv::THRESH_OTSU);
    return processed;
}

// Función principal para leer códigos de barras desde una imagen
std::string BarcodeReader::readBarcode(const cv::Mat& image) {
    // Preprocesar la imagen
    cv::Mat processedImage = preprocessImage(image);

    // Inicializar el scanner de ZBar
    zbar::ImageScanner scanner;
    scanner.set_config(zbar::ZBAR_NONE, zbar::ZBAR_CFG_ENABLE, 1);

    // Convertir la imagen OpenCV a una imagen compatible con ZBar
    zbar::Image zbarImage(processedImage.cols, processedImage.rows, "Y800", processedImage.data, processedImage.cols * processedImage.rows);

    // Escanear la imagen en busca de códigos de barras
    int n = scanner.scan(zbarImage);
    std::cout << n << " barcode(s) found" << std::endl;
    
    // Si se encuentra un código de barras, devolver su contenido
    for (zbar::Image::SymbolIterator symbol = zbarImage.symbol_begin(); symbol != zbarImage.symbol_end(); ++symbol) {
        return symbol->get_data();  // Devolver el primer código de barras encontrado
    }

    return "";  // Si no se encuentra ningún código de barras
}
