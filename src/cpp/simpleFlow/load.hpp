#ifndef _LOAD_HPP_
#define _LOAD_HPP_

// Include needed libraries
#include <iostream>
#include "types.hpp"  // Importing c_type and d_type
#include "conv2d.hpp" // Importing architecture variables

using namespace std;

void load_image(
    // Input
    ifstream& source

    // Output
    // c_type data_out[C_OUT*C_IN*ROWS*COLUMNS]
);

void load_weight(
    // Input
    ifstream source,

    // Output
    c_type coeffs_out[C_OUT*C_IN*ROWS*COLUMNS]
);

void load_biases(
    // Input
    ifstream source,

    // Output
    c_type coeffs_out[C_OUT*C_IN*ROWS*COLUMNS]
);

void load_all(); // TODO


#endif