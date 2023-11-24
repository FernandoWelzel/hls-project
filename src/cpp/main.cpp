#include <iostream>
#include <unistd.h>
#include <getopt.h>

#include "formatting.h"

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

    // Returns zero in case of no errors    
    return 0;
}
