#!/bin/bash

# Download and install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
rm miniconda.sh

# Initialize conda
eval "$($HOME/miniconda/bin/conda shell.bash hook)"
conda init

# Create a new conda environment named venv
conda create -n venv python=3.8 -y

# Activate the environment
echo "conda activate venv" >> ~/.bashrc
source ~/.bashrc
