// Include files for data types
#include "TYPES.hpp"
#include "POOL2D.hpp"

// Main macro for convolution definition
#define POOL2D_HARDWARE_MACRO(NAME, ROWS, COLUMNS, CHANNELS, K_X, K_Y) \
void HARDWARE_##NAME( \
    d_type data_in[CHANNELS*ROWS*COLUMNS], \
    d_type data_out[CHANNELS*ROWS*COLUMNS/4] \
) { \
    d_type largest; \
    d_type pixel; \
    int x_index; \
    int y_index; \
    CHANNEL_OUT:for(int c = 0; c < CHANNELS; c++) { \
        ROW:for(int x = 0; x < ROWS; x++) { \
            COLUMN:for(int y = 0; y < COLUMNS; y++) { \
                largest = 0; \
                AXIS_KERNEL_X:for(int m = 0; m < K_X; m++) { \
                    x_index = x*2 + m; \
                    X_BOUNDS:if(x_index >= 0 && x_index < ROWS) { \
                        AXIS_KERNEL_Y:for(int n = 0; n < K_Y; n++) { \
                            y_index = y*2 + n; \
                            Y_BOUNDS:if(y_index >= 0 && y_index < COLUMNS) { \
                                pixel = data_in[feature_index(c, m, n, K_X, K_Y)]; \
                                LARGEST_BOUNDS:if(largest < pixel) { \
                                    largest = pixel; \
                                } \
                            } \
                        } \
                    } \
                } \
                data_out[output_index(c, x, y, ROWS, COLUMNS)] = largest; \
            } \
        } \
    } \
} \

// Defining desings as sub-blocks
#pragma hls_design hidden

// Defining the function calling
POOL2D_HARDWARE_MACRO(POOL1, ROWS_CONV1, COLUMNS_CONV1, CHANNELS_OUT_CONV1, KERNEL_X, KERNEL_Y);
POOL2D_HARDWARE_MACRO(POOL2, ROWS_CONV2, COLUMNS_CONV2, CHANNELS_OUT_CONV2, KERNEL_X, KERNEL_Y);
POOL2D_HARDWARE_MACRO(POOL3, ROWS_CONV3, COLUMNS_CONV3, CHANNELS_OUT_CONV3, KERNEL_X, KERNEL_Y);