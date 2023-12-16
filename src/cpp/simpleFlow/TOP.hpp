#ifndef __TOP_HPP__
#define __TOP_HPP__

// Include files for data types
#include "TYPES.hpp"

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
);

#endif
