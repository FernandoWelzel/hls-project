// Include files for data types
#include "TOP.hpp"
#include "TYPES.hpp"

#include <iostream>
#include <gtest/gtest.h>

void fill_with(c_type *array, int value, int size) {
    for (int i = 0; i < size; i++) {
        array[i] = value;
    }
}

TEST(top_test, top_minimal)
{
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

    // Initializing values of coeffs
    fill_with(coeffs_conv1, 1, COEFFS_CONV1);
    fill_with(coeffs_conv2, 1, COEFFS_CONV2);
    fill_with(coeffs_conv3, 1, COEFFS_CONV3);
    fill_with(bias_conv1, 1, CHANNELS_OUT_CONV1);
    fill_with(bias_conv2, 1, CHANNELS_OUT_CONV2);
    fill_with(bias_conv3, 1, CHANNELS_OUT_CONV3);
    fill_with(coeffs_dense, 1, OUTPUT_SIZE_DENSE*INPUT_SIZE_DENSE);
    fill_with(bias_dense, 1, OUTPUT_SIZE_DENSE);

    // Test main loop
    HARDWARE_TOP(
        data_in,
        coeffs_conv1,
        bias_conv1,
        coeffs_conv2,
        bias_conv2,
        coeffs_conv3,
        bias_conv3,
        coeffs_dense,
        bias_dense,
        data_out
    );
}

// Runs all TEST functions declared at this file
int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
