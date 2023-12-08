# hls-project

This project aims to implement a CNN accelerator in FPGA for the CIFAR-10 dataset. To do so, the network was first modeled in Python by creating a basic TensorFlow clone (simpleFlow). The Python implementation was then transformed in a C model, that will be used to generate hardware using High Level Synthesis (HLS) tools.

# Python

To understand the basic inner workings of a convolutional neural network, a python model was implemented.

## Running

The python project can be run going to `src/python` and executing the `main.py` script. This will make the predictions for the `S` first images of the dataset with the previosly loaded weights. The following is an example of execution running the 3x3 kernel architecture for the first 10 test images. Note that to standardize the python envirroment we have to create a virtual envirroment.

```sh
cd src/python
make venv
source venv/bin/activate
python main.py --steps 10 --type 3x3
```

To make an inference for an specific image use the following command. This will perform the inference for 42th image of the test dataset and plot the results using Matplotlib.

```sh
cd src/python
python inference.py --image 42 --plot
```

# Testing

Basic unit tests have been implemented for the python version. To run the python testing scripts you shoul place yourself in the python virtual envirroment and run the command `pytest`. The following is an example of execution of the tests.

```sd
cd src/python
source venv/bin/activate
pytest test.py
```

# C++

# Compiling

The project can be compiled using `CMake`. To do so, create a `build` folder and run the project from there. Here is an example of compilation.

```sh
mkdir build
cd build
cmake ..
make
```

# Things to do

- [ ] C++ hardware: General functions that are to be synthesizable
  - [ ] Convolution -> CONV_HARDWARE
  - [ ] Maxpooling -> POOL_HARDWARE
  - [ ] Dense -> DENSE_HARDWARE
  - [ ] Top -> TOP_HARDWARE : Integration of all functions
- [ ] C++ testbench - Should be CCS_MAIN(): Reads images and coefficients and supply them to network and compare the results
