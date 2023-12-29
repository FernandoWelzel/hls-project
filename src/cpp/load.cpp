// Include needed libraries
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include "load.hpp"

#include "CONFIG.hpp"
#include "TYPES.hpp"

#define IMAGE_SIZE (CHANNELS_IN_CONV1*ROWS_CONV1*COLUMNS_CONV1)

using namespace std;

template <typename T>
void read_and_convert(T* &array, size_t size, FILE *file) {
    // Allocating memory for the array to be read 
    array = static_cast<T*>(new T[size]);
    
    // Temporary double read from image file
    double temp;

    // Looping thought array reading and converting each value
    for (size_t i = 0; i < size; ++i) {
        fread(&temp, sizeof(double), 1, file);
        array[i] = temp;
    }
}

Image::Image(char *file_path) {
    // Open the binary file for reading
    FILE *file = fopen(file_path, "rb");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    // Allocate memory for the array in C
    label = (long int *)malloc(sizeof(long int));

    // Read the data into the C array
    fread(label, sizeof(long int), 1, file);

    // Reading image
    read_and_convert<d_type>(data, IMAGE_SIZE, file);

    // Close the file
    fclose(file);
}

Image::~Image() {
    // Dealocating pointers
    delete[] label;
    delete[] data;
}

// TODO: Fix horrible code
Weigths::Weigths(char *file_path) {
    // Open the binary file for reading
    FILE *file = fopen(file_path, "rb");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    // Read memory for each coefficient in order
    read_and_convert<c_type>(weights_conv1, COEFFS_CONV1, file);
    read_and_convert<c_type>(weights_conv2, COEFFS_CONV2, file);
    read_and_convert<c_type>(weights_conv3, COEFFS_CONV3, file);
    read_and_convert<c_type>(weights_dense, INPUT_SIZE_DENSE*OUTPUT_SIZE_DENSE, file);

    read_and_convert<c_type>(bias_conv1, CHANNELS_OUT_CONV1, file);
    read_and_convert<c_type>(bias_conv2, CHANNELS_OUT_CONV2, file);
    read_and_convert<c_type>(bias_conv3, CHANNELS_OUT_CONV3, file);
    read_and_convert<c_type>(bias_dense, OUTPUT_SIZE_DENSE, file);

    // Close the file
    fclose(file);
}

Weigths::~Weigths() {
    // Dealocating pointers
    delete[] weights_conv1;
    delete[] weights_conv2;
    delete[] weights_conv3;
    delete[] weights_dense;

    delete[] bias_conv1;
    delete[] bias_conv2;
    delete[] bias_conv3;
    delete[] bias_dense;
}
