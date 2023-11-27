# hls-project

This project aims to implement a CNN accelerator in FPGA for the CIFAR-10 dataset. To do so, the network was first modeled in Python by creating a basic TensorFlow clone (simpleFlow). The Python implementation was then transformed in a C model, that will be used to generate hardware using High Level Synthesis (HLS) tools.

# Running

The python project can be run going to `src/python` and executing the `main.py` script. This will make the predictions for the `S` first images of the dataset with the previosly loaded weights. The following is an example of execution running the 3x3 kernel architecture for the first 10 test images.

```sh
cd src/python
python main.py --steps 10 --type 3x3
```

To make an inference for an specific image use the following command. This will perform the inference for 42th image of the test dataset and plot the results using Matplotlib.

```sh
cd src/python
python inference.py --image 42 --plot
```
