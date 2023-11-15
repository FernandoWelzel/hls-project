# hls-project

This project aims to implement a CNN accelerator in FPGA for the CIFAR-10 dataset. To do so, the network was first modeled in Python by creating a basic TensorFlow clone (simpleFlow). The Python implementation was then transformed in a C model, that will be used to generate hardware using High Level Synthesis (HLS) tools.
