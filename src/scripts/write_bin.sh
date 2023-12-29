#!/bin/bash

# Check if the maximum value is provided as a command-line argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <max_value>"
    exit 1
fi

# Get the maximum value from the command-line argument
max_value=$1

# Writing weights into desired file
python ../python/write_weigths.py -o ../../data/processed/weights.bin

# Writing images from zero to IMAGE into the folder
for ((N=0; N<=max_value; N++)); do
    python ../python/write_image.py -o ../../data/processed/image_$N.bin -i $N
done
