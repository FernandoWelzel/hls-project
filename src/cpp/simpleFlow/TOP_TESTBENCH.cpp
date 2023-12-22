
#include "TYPES.hpp"
#include "TOP.hpp"

#include <fstream>
#include <iostream>
#include <iomanip>

#include "mc_scverify.h"

CCS_MAIN(int argc, char **argv) {
    // Test variables
    d_type data_in[CHANNELS_IN_CONV1*ROWS_CONV1*COLUMNS_CONV1];
    
    c_type coeffs_conv1[COEFFS_CONV1];
    c_type bias_conv1[CHANNELS_OUT_CONV1];

    c_type coeffs_conv2[COEFFS_CONV2];
    c_type bias_conv2[CHANNELS_OUT_CONV2];

    c_type coeffs_conv3[COEFFS_CONV3];
    c_type bias_conv3[CHANNELS_OUT_CONV3];

    c_type coeffs_dense[OUTPUT_SIZE_DENSE*INPUT_SIZE_DENSE];
    c_type bias_dense[OUTPUT_SIZE_DENSE];

    ac_channel<d_type> data_out;

    // TODO: Load coefficients and image
    

    // Test main loop
	CCS_DESIGN(CONV_HARDWARE)(data_in, coeffs_in, bias_in, data_out);

    // Printing ordered result
    for(int i = 0; i < OUTPUT_SIZE_DENSE; i++) {
        std::cout << data_out[i*ROWS+j] << " ";
    }

	CCS_RETURN(0);
}
