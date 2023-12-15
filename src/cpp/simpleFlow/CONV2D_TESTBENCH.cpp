// Specific definitions for this test
#define ARCHITECTURE 1
#define C_IN 1
#define ROWS 3
#define COLUMNS 3
#define C_OUT 1
#define K_X 3
#define K_Y 3

#include "CONV2D_TYPES.hpp"
#include "CONV2D.hpp"

#include <fstream>
#include <iostream>
#include <iomanip>

#include "mc_scverify.h"

CCS_MAIN(int argc, char **argv) {
    // Test variables
    d_type data_in[C_IN*ROWS*COLUMNS];
    d_type data_out[C_OUT*ROWS*COLUMNS];
    c_type coeffs_in[C_OUT*C_IN*ROWS*COLUMNS];
    c_type bias_in[C_OUT];

    // Fill with arbitrary data
    for(int i = 0; i < C_IN*ROWS*COLUMNS; i++) {
        data_in[i] = 1;
    }
    
    for(int j = 0; j < C_OUT*C_IN*ROWS*COLUMNS; j++) {
        coeffs_in[j] = 5e-1;
    }
    
    for(int k = 0; k < C_OUT; k++) {
        bias_in[k] = 1;
    }

    // Test main loop
	CCS_DESIGN(CONV_HARDWARE)(data_in, coeffs_in, bias_in, data_out);

    // Printing ordered result
    for(int i = 0; i < ROWS; i++) {
        for(int j = 0; j < COLUMNS; j++) {
            std::cout << data_out[i*ROWS+j] << " ";
        }
        std::cout << std::endl;
    }

	CCS_RETURN(0);
}
