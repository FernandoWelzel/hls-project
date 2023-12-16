#ifndef __DENSE_HPP__
#define __DENSE_HPP__

// Include files for data types
#include "TYPES.hpp"

// Building macros
#define DENSE_HARDWARE_INCLUDE(NAME, INPUT_SIZE, OUTPUT_SIZE) \
void HARDWARE_##NAME##( \
    d_type data_in[INPUT_SIZE], \
    c_type coeffs_in[OUTPUT_SIZE*INPUT_SIZE], \
    c_type bias_in[OUTPUT_SIZE], \
    d_type *data_out \
) 

// Defining the function calling
DENSE_HARDWARE_INCLUDE(DENSE, 180, 10);

#endif
