#ifndef __CONV2D_HPP__
#define __CONV2D_HPP__

// Include files for data types
#include "TYPES.hpp"
#include "CONFIG.hpp"

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
CONV_HARDWARE_INCLUDE(CONV1, ROWS_CONV1, COLUMNS_CONV1, CHANNELS_IN_CONV1, CHANNELS_OUT_CONV1, KERNEL_X, KERNEL_Y);
CONV_HARDWARE_INCLUDE(CONV2, ROWS_CONV2, COLUMNS_CONV2, CHANNELS_IN_CONV2, CHANNELS_OUT_CONV2, KERNEL_X, KERNEL_Y);
CONV_HARDWARE_INCLUDE(CONV3, ROWS_CONV3, COLUMNS_CONV3, CHANNELS_IN_CONV3, CHANNELS_OUT_CONV3, KERNEL_X, KERNEL_Y);

#endif
