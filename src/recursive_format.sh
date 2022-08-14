#!/bin/bash

# need to activate conda environment with black installed
source ~/anaconda3/etc/profile.d/conda.sh
conda activate wwn

# finds path to all python files recursively and
# runs black on them individually
# {} + won't work if over 50 files found
find . -regex ".*.py" -exec black {} \;
find . -regex ".*.html" -exec npx prettier -w {} \;
find . -regex ".*.js" -exec npx prettier -w {} \;

# I don't want to use pre-commit
