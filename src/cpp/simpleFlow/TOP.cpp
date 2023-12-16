// Include files for data types
#include "TYPES.hpp"
#include "TOP.hpp"
#include "CONV2D.hpp"
#include "POOL2D.hpp"
#include "DENSE.hpp"

#include <iostream>

// Main design
#pragma hls_design top
void HARDWARE_TOP(
    // Input
    d_type data_in[24*24*3],
    
    // Configuration values
    c_type coeffs1_in[3*3*3*64],
    c_type bias1_in[64],

    c_type coeffs2_in[3*3*64*32],
    c_type bias2_in[32],
    
    c_type coeffs3_in[3*3*32*20],
    c_type bias3_in[20],

    c_type coeffs_dense_in[3*3*20*10],
    c_type bias_dense_in[10],

    // Output
    ac_channel<d_type> data_out
)
{
    // Intermidiate variables
    d_type data_conv1[24*24*64];
    d_type data_conv2[12*12*32];
    d_type data_conv3[6*6*20];
    
    d_type data_pool1[12*12*64];
    d_type data_pool2[6*6*32];
    d_type data_pool3[3*3*20];

    d_type data_dense[10];

    // Processing
    HARDWARE_CONV1(data_in, coeffs1_in, bias1_in, data_conv1);
    HARDWARE_POOL1(data_conv1, data_pool1);
    
    HARDWARE_CONV2(data_pool1, coeffs2_in, bias2_in, data_conv2);
    HARDWARE_POOL2(data_conv2, data_pool2);
    
    HARDWARE_CONV3(data_pool2, coeffs3_in, bias3_in, data_conv3);
    HARDWARE_POOL3(data_conv3, data_pool3);

    HARDWARE_DENSE(data_pool3, coeffs_dense_in, bias_dense_in, data_dense);

    d_type max = 0;

    // Finding max
    for(int i = 0; i < 10; i++) {
        if(data_dense[i] > max) {
            max = data_dense[i];
        }
    }

    // Writing final result - Wrong: It should be the index
    data_out.write(max);
}