// Include needed libraries
#include <iostream>
#include <fstream> 
#include "load.hpp"
#include <string>
#include <sstream>

using namespace std;

double bytesToFloat(byte b0, byte b1, byte b2, byte b3, byte b4, byte b5, byte b6, byte b7) 
{ 
    byte byte_array[] = { b7, b6, b5, b4, b3, b2, b1, b0 };
    float result;
    std::copy(reinterpret_cast<const char*>(&byte_array[0]),
              reinterpret_cast<const char*>(&byte_array[7]),
              reinterpret_cast<char*>(&result));
    return result;
}



void load_image(
    // Input
    ifstream& source

    // Output
    // c_type data_out [C_OUT*C_IN*ROWS*COLUMNS]
){
    
    // Check if the file is opened
    if (!source.is_open()){
        cerr << "ERROR: Unable to open the source file" << endl;
        return;
    }
    
    const int labelSize = 3;
    char buffer[labelSize];

    const int groupSize = 8;                // one group represents one float of 64bits (== 8bytes)
    const int numGroups = 64 / groupSize;   
    char groupBuffer[groupSize];

    source.read(buffer, labelSize);

    for (int i = 0; i < labelSize; ++i) {
        std::cout << "Byte " << i + 1 << ": " << static_cast<int>(buffer[i]) << std::endl;
    }

    std::cout << "AFTER FIRST 3 BYTES (LABEL)" << std::endl; 

    // std::ostringstream tmp;
    double aux;
    byte tmp[8];

    for (int i = 0; i < numGroups; ++i) {
        source.read(groupBuffer, groupSize);
        // Process the data in the group buffer
        std::cout << "Group " << i + 1 << ": ";
        for (int j = 0; j < groupSize; ++j) {
            // reading: should append 8 bytes to then transform them into one float64 bits
            tmp [j] = static_cast<byte>(groupBuffer[j]);
            // string.append(string, groupBuffer[j]);
            // tmp[j] = groupBuffer[j];
            // std::cout << static_cast<double>(groupBuffer[j]) << " ";
        }
        
        aux = bytesToFloat(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7]);
        // aux = tmp.str();

        std::cout << aux;

        std::cout << std::endl;
        }


    string mystring;
    // source >> mystring;
    cout << mystring << endl;

};


