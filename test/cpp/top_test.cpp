// Include files for data types
#include "TOP.hpp"
#include "TYPES.hpp"

#include <iostream>
#include <gtest/gtest.h>

TEST(top_test, top_minimal)
{
    // Test variables
    // d_type data_in[C_IN*ROWS*COLUMNS];
    // d_type data_out[C_OUT*ROWS*COLUMNS];
    // c_type coeffs_in[C_OUT*C_IN*ROWS*COLUMNS];
    // c_type bias_in[C_OUT];

    
    // // Fill with arbitrary data
    // for(int i = 0; i < C_IN*ROWS*COLUMNS; i++) {
    //     data_in[i] = 1;
    // }
    
    // for(int j = 0; j < C_OUT*C_IN*ROWS*COLUMNS; j++) {
    //     coeffs_in[j] = 5e-1;
    // }
    
    // for(int k = 0; k < C_OUT; k++) {
    //     bias_in[k] = 1;
    // }

    // Test main loop
    // HARDWARE_TOP(data_in, coeffs_in, bias_in, data_out);
}

// Runs all TEST functions declared at this file
int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
