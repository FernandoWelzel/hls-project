// Include files for data types
#include "TYPES.hpp"
#include "CONFIG.hpp"
#include "CONV2D.hpp"

// Main macro for convolution definition
#define CONV_HARDWARE_MACRO(NAME, ROWS, COLUMNS, C_IN, C_OUT, K_X, K_Y) \
void HARDWARE_##NAME( \
    d_type data_in[C_IN*ROWS*COLUMNS], \
    c_type coeffs_in[C_OUT*C_IN*K_X*K_Y], \
    c_type bias_in[C_OUT], \
    d_type *data_out \
) { \
    a_type sum; \
    c_type weight; \
    d_type pixel; \
    int x_index; \
    int y_index; \
    CHANNEL_OUT:for(int c_out = 0; c_out < C_OUT; c_out++) { \
        ROW:for(int x = 0; x < ROWS; x++) { \
            COLUMN:for(int y = 0; y < COLUMNS; y++) { \
                sum = bias_in[c_out]; \
                CHANNEL_IN:for(int c_in = 0; c_in < C_IN; c_in++) { \
                    KERNEL_X_AXIS:for(int m = 0; m < K_X; m++) { \
                        x_index = kernel_index(x, m, K_X); \
                        X_BOUNDS:if(x_index >= 0 && x_index < ROWS) { \
                            KERNEL_Y_AXIS:for(int n = 0; n < K_Y; n++) { \
                                y_index = kernel_index(y, n, K_Y); \
                                Y_BOUNDS:if(y_index >= 0 && y_index < COLUMNS) { \
                                    weight = coeffs_in[coeff_index(c_out, c_in, K_X, K_Y, m, n)]; \
                                    pixel = data_in[feature_index(c_in, m, n, K_X, K_Y)]; \
                                    sum += weight*pixel; \
                                    std::cout << sum << std::endl; \
                                } \
                            } \
                        } \
                    } \
                } \
                RELU:if(sum < 0) sum = 0; \
                data_out[output_index(c_out, x, y, ROWS, COLUMNS)] = sum; \
            } \
        } \
    } \
} \

// Defining desings as sub-blocks
#pragma hls_design hidden

// Defining the each type of convolution
CONV_HARDWARE_MACRO(CONV1, ROWS_CONV1, COLUMNS_CONV1, CHANNELS_IN_CONV1, CHANNELS_OUT_CONV1, KERNEL_X, KERNEL_Y);
CONV_HARDWARE_MACRO(CONV2, ROWS_CONV2, COLUMNS_CONV2, CHANNELS_IN_CONV2, CHANNELS_OUT_CONV2, KERNEL_X, KERNEL_Y);
CONV_HARDWARE_MACRO(CONV3, ROWS_CONV3, COLUMNS_CONV3, CHANNELS_IN_CONV3, CHANNELS_OUT_CONV3, KERNEL_X, KERNEL_Y);
