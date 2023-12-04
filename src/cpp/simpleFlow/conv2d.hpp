#ifndef CONV2D_HPP
#define CONV2D_HPP

#include <iostream>
#include <vector>
#include <stdexcept>

#include "layer.h"

class Conv2D : public Layer {
public:
    // Constructor
    Conv2D(const std::tuple<int, int>& kernel_size, const std::tuple<int, int, int>& input_shape,
        const std::tuple<int, int, int>& output_shape, const std::string& name);
    
    // Process neural network
    std::vector<std::vector<std::vector<double>>> forward(const std::vector<std::vector<std::vector<double>>>& feature_map);

    // Load weights and biases into private variables
    void load_weights(const std::vector<std::vector<std::vector<std::vector<double>>>>& weights,
        const std::vector<double>& biases);

private:
    std::tuple<int, int> kernel_size;
    std::tuple<int, int, int> input_shape;
    std::tuple<int, int, int> output_shape;
    std::vector<std::vector<std::vector<std::vector<double>>>> weights;
    std::vector<double> bias;
};

#endif