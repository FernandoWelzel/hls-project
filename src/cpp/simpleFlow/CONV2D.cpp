// Include files for data types
#include "CONV2D_TYPES.hpp"
#include "CONV2D.hpp"

#include <iostream>

// Main design
#pragma hls_design hidden
void CONV_HARDWARE(
    // Input
    d_type data_in[C_IN*ROWS*COLUMNS],
    c_type coeffs_in[C_OUT*C_IN*ROWS*COLUMNS],
    c_type bias_in[C_OUT],

    // Output
    d_type *data_out
)
{
    // General variables
    a_type sum;
    c_type weight;
    d_type pixel;

    // Keep track of current position
    int x_index;
    int y_index;

    // Loop though all pixels
    CHANNEL_OUT:for(int c_out = 0; c_out < C_OUT; c_out++) {
        ROW:for(int x = 0; x < ROWS; x++) {
            COLUMN:for(int y = 0; y < COLUMNS; y++) {
                // Initializing sum
                sum = bias_in[c_out];

                // Compute each pixel
                CHANNEL_IN:for(int c_in = 0; c_in < C_IN; c_in++) {
                    KERNEL_X:for(int m = 0; m < K_X; m++) {
                        x_index = index(x, m, K_X);
                        
                        // Check if row is out of bounds
                        X_BOUNDS:if(x_index >= 0 && x_index < ROWS) {
                            KERNEL_Y:for(int n = 0; n < K_Y; n++) {
                                y_index = index(y, n, K_Y);

                                // Check the if value is out of bounds
                                Y_BOUNDS:if(y_index >= 0 && y_index < COLUMNS) {
                                    weight = coeffs_in[coeff_index(c_out, c_in, m, n)];
                                    pixel = data_in[feature_index(c_in, m, n)];

                                    sum += weight*pixel;
                                }
                            }
                        }
                    }
                }

                // Applies ReLU
                RELU:if(sum < 0) sum = 0;

                data_out[output_index(c_out, x, y)] = sum;
            }        
        }
    }
}