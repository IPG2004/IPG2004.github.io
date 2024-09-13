// barcode_reader.h
#ifndef BARCODE_READER_H
#define BARCODE_READER_H

#include <string>
#include <opencv2/opencv.hpp>

class BarcodeReader {
public:
    BarcodeReader();  // Constructor
    ~BarcodeReader(); // Destructor

    // Método para leer el código de barras desde una imagen
    std::string readBarcode(const cv::Mat& image);

private:
    // Método auxiliar para procesar la imagen
    cv::Mat preprocessImage(const cv::Mat& image);
};

#endif // BARCODE_READER_H
