#ifndef __CONV2D_HPP__
#define __CONV2D_HPP__

// Include files for data types
#include "TYPES.hpp"

// Functional macros
#define kernel_index(x_y, m_n, kernel_x_y) (x_y+m_n-(kernel_x_y-1)/2)
#define coeff_index(c_out, c_in, k_x, k_y, m, n) (c_out*c_in*k_x*k_y + c_in*k_x*k_y + m*k_y + n)
#define feature_index(c_in, m, n, k_x, k_y) (c_in*k_x*k_y + m*k_y + n)
#define output_index(c_out, x, y, rows, columns) (c_out*rows*columns + x*columns + y)

// Building macros
#define CONV_HARDWARE_INCLUDE(NAME, ROWS, COLUMNS, C_IN, C_OUT, K_X, K_Y) \
void HARDWARE_##NAME( \
    d_type data_in[C_IN*ROWS*COLUMNS], \
    c_type coeffs_in[C_OUT*C_IN*K_X*K_Y], \
    c_type bias_in[C_OUT], \
    d_type *data_out \
)

// Defining the function calling
CONV_HARDWARE_INCLUDE(CONV1, 24, 24, 3, 64, 3, 3);
CONV_HARDWARE_INCLUDE(CONV2, 12, 12, 64, 32, 3, 3);
CONV_HARDWARE_INCLUDE(CONV3, 6, 6, 32, 20, 3, 3);

#endif
