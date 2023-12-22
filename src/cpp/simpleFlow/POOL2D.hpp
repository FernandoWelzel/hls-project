#ifndef __POOL2D_HPP__
#define __POOL2D_HPP__

// Include files for data types
#include "TYPES.hpp"

// Functional macros
#define kernel_index(x_y, m_n, kernel_x_y) (x_y+m_n-(kernel_x_y-1)/2)
#define coeff_index(c_out, c_in, k_x, k_y, m, n) (c_out*c_in*k_x*k_y + c_in*k_x*k_y + m*k_y + n)
#define feature_index(c_in, m, n, k_x, k_y) (c_in*k_x*k_y + m*k_y + n)
#define output_index(c_out, x, y, rows, columns) (c_out*rows*columns + x*columns + y)

// Building macros
#define POOL2D_HARDWARE_INCLUDE(NAME, ROWS, COLUMNS, CHANNELS, K_X, K_Y) \
void HARDWARE_##NAME( \
    d_type data_in[CHANNELS*ROWS*COLUMNS], \
    d_type *data_out \
) \

// Defining the function calling
POOL2D_HARDWARE_INCLUDE(POOL1, 24, 24, 64, 3, 3);
POOL2D_HARDWARE_INCLUDE(POOL2, 12, 12, 32, 3, 3);
POOL2D_HARDWARE_INCLUDE(POOL3,  6,  6, 20, 3, 3);

#endif
