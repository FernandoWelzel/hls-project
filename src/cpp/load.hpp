#ifndef _LOAD_HPP_
#define _LOAD_HPP_

// Include needed libraries
#include <iostream>

#include "TYPES.hpp" // Importing c_type and d_type
#include "CONV2D.hpp" // Importing architecture variables
#include "CONFIG.hpp"

using namespace std;

class Image {
public:
    long int *label;
    d_type *data;

    Image(char *file_path);
    ~Image();
};

class Weigths {
public:
    c_type *weights_conv1;
    c_type *weights_conv2;
    c_type *weights_conv3;
    c_type *weights_dense;

    c_type *bias_conv1;
    c_type *bias_conv2;
    c_type *bias_conv3;
    c_type *bias_dense;

    Weigths(char *file_path);
    
    ~Weigths();
};

#endif