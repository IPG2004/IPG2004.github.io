// test_barcode_reader.cc
#include "barcode_reader.h"
#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // Ruta a la imagen que contiene el código de barras
    std::string imagePath = "/home/ipg/Imágenes/barcode.png";  // Cambia esta ruta a una imagen válida
    cv::Mat image = cv::imread(imagePath);

    if (image.empty()) {
        std::cerr << "Error: Could not open image file." << std::endl;
        return -1;
    }

    // Crear el lector de códigos de barras
    BarcodeReader reader;

    // Leer el código de barras de la imagen
    std::string barcodeData = reader.readBarcode(image);

    // Mostrar el resultado
    if (!barcodeData.empty()) {
        std::cout << "Barcode Data: " << barcodeData << std::endl;
    } else {
        std::cout << "No barcode detected." << std::endl;
    }

    return 0;
}
