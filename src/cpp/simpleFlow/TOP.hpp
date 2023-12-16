#ifndef __TOP_HPP__
#define __TOP_HPP__

// Include files for data types
#include "TYPES.hpp"

void TOP (
    // Input
    d_type data_in[C_IN*ROWS*COLUMNS],
    c_type coeffs_in[C_OUT*C_IN*ROWS*COLUMNS],
    c_type bias_in[C_OUT],

    // Output
    d_type *data_out
);

#endif
