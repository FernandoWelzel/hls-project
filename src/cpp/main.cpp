#include <iostream>
#include <unistd.h>
#include <getopt.h>
#include <fstream>

#include "TOP.hpp"

#include "formatting.hpp"
#include "load.hpp"

using namespace std;

// Usage message to be displayed if help required
void printUsage(char* argv0) {
    COLOR("USAGE:" << argv0 << " [options] filename", BLUE_TEXT);
    COLOR("Options:", RESET_COLOR);
    COLOR("  -h         Display this help message", RESET_COLOR);
    COLOR("  -v         Components print message each time they simulates", RESET_COLOR);
    COLOR("  -s [STEPS] Number of simulation steps", RESET_COLOR);
}

// Gets a platform path from the first string, builds it, and simulates it
int main(int argc, char* argv[]) {
    int option;

    // Default values for options
    int help_flag = 0;
    int verbose_flag = 0;
    int simulation_steps = 10;
    
    // Parse command-line options using getopt
    while ((option = getopt(argc, argv, "hvs:")) != -1) {
        switch (option) {
            case 'v':
                verbose_flag = 1;
                break;

            case 'h':
                help_flag = 1;
                break;
            
            case 's':
                simulation_steps = atoi(optarg);
                break;
            
            default:
                // Printing error/help message
                cout << endl; printUsage(argv[0]); cout << endl;

                ERROR("Unknown of malformated option"); return 1;
        }
    }

    // Prints help if necessary
    if (help_flag) {
        printUsage(argv[0]);
        return 0;
    }

    // Initializing file path
    char image_path[] = "./processed/image_0.bin";
    char weigths_path[] = "./processed/weights.bin";

    // Creating image from the image path    
    Image my_image(image_path);

    // Loading weigths from file
    Weigths my_weigths(weigths_path);

    // Declaring output variable
    ac_channel<d_type> data_out;

    // Computing values using the custom hardware
    HARDWARE_TOP(
        // Input image values
        my_image.data,

        // Coefficients
        my_weigths.weights_conv1,
        my_weigths.bias_conv1,
        
        my_weigths.weights_conv2,
        my_weigths.bias_conv2,
        
        my_weigths.weights_conv3,
        my_weigths.bias_conv3,
        
        my_weigths.weights_dense,
        my_weigths.bias_dense,

        // Output value
        data_out
    );
    
    return 0;
}
