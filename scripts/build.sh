#!/bin/sh

. $(conda info --base)/etc/profile.d/conda.sh
conda env update -f ./scripts/environment.yml
