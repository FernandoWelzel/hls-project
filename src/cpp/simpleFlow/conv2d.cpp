#include "conv2d.hpp"

// Constructor
Conv2D::Conv2D(const std::tuple<int, int>& kernel_size, const std::tuple<int, int, int>& input_shape, 
    const std::tuple<int, int, int>& output_shape, const std::string& name)
    : Layer(name), kernel_size(kernel_size), input_shape(input_shape), output_shape(output_shape) {
    
    // Checking kernel size is odd
    for (int size : {std::get<0>(kernel_size), std::get<1>(kernel_size)}) {
        if(size%2 != 1) {
            throw std::invalid_argument("Kernel size must be odd");
        }
    }

    // Base parameters
    this->kernel_size = kernel_size;
    this->output_shape = output_shape;
    this->input_shape = input_shape;

    // Internal matrices
    this->weights.resize(std::get<0>(output_shape), std::vector<std::vector<std::vector<double>>>(
        std::get<0>(input_shape), std::vector<std::vector<double>>(
        std::get<0>(kernel_size), std::vector<double>(std::get<1>(kernel_size), 1.0))));

    this->bias.resize(std::get<0>(output_shape), 1.0);
}

// Method to process feature map
std::vector<std::vector<std::vector<double>>> Conv2D::forward(const std::vector<std::vector<std::vector<double>>>& feature_map) {
    // If input is 2 dimensional, transform into 3 dimensions
    std::vector<std::vector<std::vector<double>>> input_feature_map = feature_map;
    if (feature_map.size() == 2) {
        input_feature_map = {{{feature_map[0][0], feature_map[0][1]}}};
    }

    std::vector<std::vector<std::vector<double>>> output(std::get<0>(output_shape), std::vector<std::vector<double>>(std::get<1>(output_shape), std::vector<double>(std::get<2>(output_shape), 0.0)));

    int rows = std::get<1>(output_shape);
    int columns = std::get<2>(output_shape);
    int channels_out = std::get<0>(output_shape);
    int channels_in = std::get<0>(input_shape);
    int kernelX = std::get<0>(kernel_size);
    int kernelY = std::get<1>(kernel_size);

    // Compute each channel
    for (int c_out = 0; c_out < channels_out; ++c_out) {
        // Compute each row
        for (int x = 0; x < rows; ++x) {
            // Compute each column
            for (int y = 0; y < columns; ++y) {
                // Initializing sum
                double sum = bias[c_out];

                // Iterating through input layers of the kernel
                for (int c_in = 0; c_in < channels_in; ++c_in) {
                    // Iterate through X of kernel
                    for (int m = 0; m < kernelX; ++m) {
                        int x_index = x + m - (kernelX - 1) / 2;
                        bool x_out_of_bound = (x_index < 0) || (x_index >= std::get<1>(input_shape));

                        // Iterate through Y of kernel
                        for (int n = 0; n < kernelY; ++n) {
                            int y_index = y + n - (kernelY - 1) / 2;
                            bool y_out_of_bound = (y_index < 0) || (y_index >= std::get<2>(input_shape));

                            bool out_of_bounds = x_out_of_bound || y_out_of_bound;

                            if (!out_of_bounds) {
                                double weight = weights[c_out][c_in][m][n];
                                double pixel = input_feature_map[c_in][x_index][y_index];

                                sum += weight * pixel;
                            }
                        }
                    }
                }

                // Applies ReLU
                if (sum < 0)
                    sum = 0;

                output[c_out][x][y] = sum;
            }
        }
    }

    return output;
}

// Method to store weights into class
void Conv2D::load_weights(const std::vector<std::vector<std::vector<std::vector<double>>>>& weights, const std::vector<double>& biases) {
    this->weights = weights;
    this->bias = biases;
}