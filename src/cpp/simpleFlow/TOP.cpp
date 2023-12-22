// Include files for data types
#include "TYPES.hpp"
#include "TOP.hpp"
#include "CONFIG.hpp"
#include "CONV2D.hpp"
#include "POOL2D.hpp"
#include "DENSE.hpp"

#include <iostream>

// Main design
#pragma hls_design top
void HARDWARE_TOP(
    // Input
    d_type data_in[ROWS_CONV1*COLUMNS_CONV1*CHANNELS_IN_CONV1],
    
    // Configuration values
    c_type coeffs1_in[KERNEL_X*KERNEL_Y*CHANNELS_IN_CONV1*CHANNELS_OUT_CONV1],
    c_type bias1_in[CHANNELS_OUT_CONV1],

    c_type bias2_in[CHANNELS_OUT_CONV2],
    c_type coeffs2_in[KERNEL_X*KERNEL_Y*CHANNELS_IN_CONV2*CHANNELS_OUT_CONV2],
    
    c_type coeffs3_in[KERNEL_X*KERNEL_Y*CHANNELS_IN_CONV3*CHANNELS_OUT_CONV3],
    c_type bias3_in[CHANNELS_OUT_CONV3],

    c_type coeffs_dense_in[INPUT_SIZE_DENSE*OUTPUT_SIZE_DENSE],
    c_type bias_dense_in[OUTPUT_SIZE_DENSE],

    // Output
    ac_channel<d_type> data_out
)
{
    // Intermidiate variables
    d_type data_conv1[ROWS_CONV1*COLUMNS_CONV1*CHANNELS_OUT_CONV1];
    d_type data_conv2[ROWS_CONV2*COLUMNS_CONV2*CHANNELS_OUT_CONV2];
    d_type data_conv3[ROWS_CONV3*COLUMNS_CONV3*CHANNELS_OUT_CONV3];
    
    d_type data_pool1[ROWS_CONV2*COLUMNS_CONV2*CHANNELS_OUT_CONV2];
    d_type data_pool2[ROWS_CONV3*COLUMNS_CONV3*CHANNELS_OUT_CONV3];
    d_type data_pool3[INPUT_SIZE_DENSE];

    d_type data_dense[OUTPUT_SIZE_DENSE];

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
    for(int i = 0; i < OUTPUT_SIZE_DENSE; i++) {
        if(data_dense[i] > max) {
            max = data_dense[i];
        }
    }

    std::cout << "Max: " << max << std::endl;

    data_out.write(max);
}