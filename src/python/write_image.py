import argparse

from load_coeff import *
from read_dataset import *

"""
Writes CIFAR10 images into binary files.

Usage example:
    python write_image.py --output_path image_10.bin --image 10
"""
def main():
    parser = argparse.ArgumentParser(description='Writes CIFAR10 images into binary files.')

    parser.add_argument('-i', '--image', help='Number of image to write', required=False, default="0")
    parser.add_argument('-o', '--output_path', help='Path to the output file', required=True)
    parser.add_argument('-s', '--source_path', help='Path to the source file', required=False, default="../../data/cifar-10-python/cifar-10-batches-py/test_batch")

    args = parser.parse_args()

    # Writing files
    write_dataset(args.output_path, args.source_path, int(args.image))

if __name__ == "__main__":
    main()
