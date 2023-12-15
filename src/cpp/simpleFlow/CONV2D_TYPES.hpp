#ifndef __TYPES_HPP__
#define __TYPES_HPP__

#include "ac_fixed.h"
#include "ac_channel.h"

#define DATA_WIDTH 8
#define COEFF_WIDTH 16
#define HEADROOM 6

typedef ac_fixed<DATA_WIDTH,DATA_WIDTH,true,AC_RND_INF,AC_SAT> d_type ;
typedef ac_fixed<COEFF_WIDTH,1,true,AC_RND_INF,AC_SAT> c_type ;
typedef ac_fixed<DATA_WIDTH+COEFF_WIDTH+HEADROOM,DATA_WIDTH+HEADROOM+1,true> a_type ;

#endif
