#ifndef __TOP_HPP__
#define __TOP_HPP__

// Include files for data types
#include "TYPES.hpp"
#include "CONFIG.hpp"
void HARDWARE_TOP(

    // Input
    d_type data_in[ROWS_CONV1*COLUMNS_CONV1*CHANNELS_IN_CONV1],
    
    // Configuration values
    c_type coeffs1_in[KERNEL_X*KERNEL_Y*CHANNELS_IN_CONV1*CHANNELS_OUT_CONV1],
    c_type bias1_in[CHANNELS_OUT_CONV1],

    c_type coeffs2_in[KERNEL_X*KERNEL_Y*CHANNELS_IN_CONV2*CHANNELS_OUT_CONV2],
    c_type bias2_in[CHANNELS_OUT_CONV2],
    
    c_type coeffs3_in[KERNEL_X*KERNEL_Y*CHANNELS_IN_CONV3*CHANNELS_OUT_CONV3],
    c_type bias3_in[CHANNELS_OUT_CONV3],

    c_type coeffs_dense_in[INPUT_SIZE_DENSE*OUTPUT_SIZE_DENSE],
    c_type bias_dense_in[OUTPUT_SIZE_DENSE],

    // Output
    ac_channel<d_type> data_out
);

#endif
