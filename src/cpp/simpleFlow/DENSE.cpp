// Include files for data types
#include "TYPES.hpp"
#include "CONFIG.hpp"
#include "DENSE.hpp"

// Main macro for convolution definition
#define DENSE_HARDWARE_MACRO(NAME, INPUT_SIZE, OUTPUT_SIZE) \
void HARDWARE_##NAME( \
    d_type data_in[INPUT_SIZE], \
    c_type coeffs_in[OUTPUT_SIZE*INPUT_SIZE], \
    c_type bias_in[OUTPUT_SIZE], \
    d_type data_out[OUTPUT_SIZE] \
) { \
    a_type sum; \
    c_type weight; \
    d_type value; \
    OUT:for(int out = 0; out < OUTPUT_SIZE; out++) { \
        sum = bias_in[out]; \
        IN:for(int in = 0; in < INPUT_SIZE; in++) { \
            weight = coeffs_in[out*OUTPUT_SIZE+in]; \
            value = data_in[in]; \
            sum += weight*value; \
        } \
        data_out[out] = sum; \
    } \
} \

// Defining desings as sub-blocks
#pragma hls_design hidden

// Defining the each type of convolution
DENSE_HARDWARE_MACRO(DENSE, INPUT_SIZE_DENSE, OUTPUT_SIZE_DENSE);
