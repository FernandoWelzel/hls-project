// Specific definitions for this test
#define ARCHITECTURE 1
#define C_IN 3
#define ROWS 32
#define COLUMNS 32
#define C_OUT 64
#define K_X 3
#define K_Y 3

// Include files for data types
#include "conv2d.hpp"
#include "types.hpp"

#include <iostream>

// Get the values
#include <fstream>

const std::string cifar10_data_path = "../../data/cifar-10-python/cifar-10-batches-py/";

struct CIFAR10Record {
    unsigned char label;
    unsigned char pixels[3072]; // 32x32 image with 3 channels (RGB)
};

int main() {
    std::ifstream file(cifar10_data_path + "test_batch", std::ios::binary);

    if (!file.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }
    
    CIFAR10Record record;

    // Get the value image
    file.read(reinterpret_cast<char*>(&record), sizeof(CIFAR10Record));

    // Access the pixel data and label
    unsigned char label = record.label;

    std::cout << "Label: " << static_cast<int>(label) << std::endl;
   
    // Printing ordered result
    for(int c = 0; c < C_IN; c++) {
        for(int i = 0; i < ROWS; i++) {
            for(int j = 0; j < COLUMNS; j++) {
                std::cout << static_cast<unsigned int>(record.pixels[c*ROWS*COLUMNS + i*ROWS + j]) << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl << std::endl;
    }

    file.close();

    return 0;
}