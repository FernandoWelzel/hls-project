/* Variables formats - p(x, y) : c(c, x, y) : b(c)
    Data: data_in[0] = {p(0,0), p(0,1), p(0,2), ..., p(0,23), p(1,0), p(1,1), ... p(23, 23)}
    Coefficients: coeffs_in[0] = {c(0,0,0), c(0,0,0), c(0,0,2), c(0,1,0), c(0,1,1), ... c(1,0,0), ...,c(63,3,3)}
    Data types are like that b(c) - {b(0), b(1), b(2), ..., b(64)}
*/

#ifndef MAIN_HPP
#define MAIN_HPP

#include "ac_fixed.h"

void CONV_HARDWARE(
    d_type &data_in[C_IN],
    d_type &data_out[C_OUT]

    c_type &coeffs_in[C_OUT],
    c_type &bias_in[C_OUT]
)

void POOL_HARDWARE(
    d_type &data_in[C_IN],
    d_type &data_out[C_OUT]
)

void DENSE_HARDWARE(
    d_type &data_in[C_IN],
    d_type &data_out[C_OUT]

    c_type &coeffs_in[C_OUT],
    c_type &bias_in[C_OUT]
)

void TOP_HARWARE(
    d_type &data_out[C_OUT]
)

#endif