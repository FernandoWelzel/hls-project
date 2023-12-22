#include <iostream>
#include <unistd.h>
#include <getopt.h>
#include <fstream>

#include "formatting.h"
#include "simpleFlow/load.hpp"

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
    int helpFlag = 0;
    int verboseFlag = 0;
    int simulationSteps = 10;

    // Parse command-line options using getopt
    while ((option = getopt(argc, argv, "hvs:")) != -1) {
        switch (option) {
            case 'v':
                verboseFlag = 1;
                break;

            case 'h':
                helpFlag = 1;
                break;
            
            case 's':
                simulationSteps = atoi(optarg);
                break;

            default:
                // Printing error/help message
                cout << endl; printUsage(argv[0]); cout << endl;

                ERROR("Unknown of malformated option"); return 1;
        }
    }

    // Prints help if necessary
    if (helpFlag) {
        printUsage(argv[0]);
        return 0;
    }

    // cout << "[MAIN] Main was called" << endl;


    // // Get the file path:
    // const char* filePath = "teste.bin";
    // cout << "[MAIN] File path is: " << filePath << endl;
    // ifstream source_bin (filePath, ios::binary);
    
    // load_image(source_bin);


    //  if (!source_bin) {
    //     std::cerr << "[MAIN] Unable to open the file." << std::endl;
    //     return 1;
    // }
    // else {
    //     std::cout << "[MAIN] File read successfully." << std::endl;
    // }

    // // Returns zero in case of no errors    
    // return 0;

    // Specify the file name
    const char *file_name = "teste";

    // Open the binary file for reading
    FILE *file = fopen(file_name, "rb");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Allocate memory for the array in C
    long int *label = (long int *)malloc(sizeof(long int));
    double *data = (double *)malloc(sizeof(double) * 24*24*3);

    // Read the data into the C array
    fread(label, sizeof(long int), 1, file);
    fread(data, sizeof(double), 24*24*3, file);

    // Close the file
    fclose(file);

    cout << *label << endl;
    cout << data[0] << endl;

    // Free allocated memory
    free(data);

    return 0;

}
