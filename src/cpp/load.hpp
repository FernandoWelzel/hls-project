#ifndef _LOAD_HPP_
#define _LOAD_HPP_

// Include needed libraries
#include <iostream>

#include "TYPES.hpp"  // Importing c_type and d_type
#include "CONV2D.hpp" // Importing architecture variables
#include "CONFIG.hpp"

using namespace std;

void load_image(
    // Input
    ifstream& source
);

void load_weight(
    // Input
    ifstream source,

    // Output
    c_type *coeffs_out
);

void load_biases(
    // Input
    ifstream source,

    // Output
    c_type *coeffs_out
);

void load_all(); // TODO


#endif