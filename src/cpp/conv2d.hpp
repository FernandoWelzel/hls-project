#ifndef __CONV2D_HPP__
#define __CONV2D_HPP__

// Architectural definitions
#ifndef ARCHITECTURE
    #define C_IN 1
    #define ROWS 3
    #define COLUMNS 3
    #define C_OUT 1
    #define K_X 3
    #define K_Y 3
#endif

#define index(x_y, m_n, kernel_x_y) (x_y+m_n-(kernel_x_y-1)/2)
#define coeff_index(c_out, c_in, m, n) (c_out*C_IN*K_X*K_Y + c_in*K_X*K_Y + m*K_Y + n)
#define feature_index(c_in, m, n) (c_in*K_X*K_Y + m*K_Y + n)
#define output_index(c_out, x, y) (c_out*ROWS*COLUMNS + x*COLUMNS + y)

// Include files for data types
#include "FIR_TYPES.h"

void CONV_HARDWARE(
    // Input
    d_type data_in[C_IN*ROWS*COLUMNS],
    c_type coeffs_in[C_OUT*C_IN*ROWS*COLUMNS],
    c_type bias_in[C_OUT],

    // Output
    d_type *data_out
);

#endif
