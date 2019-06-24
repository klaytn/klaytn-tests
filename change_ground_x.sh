#!/bin/bash

# On macOS
files=$(git grep -l "ground-x") && echo $files | xargs -t sed -i '' 's/ground-x/klaytn/g'

# On Linux
#files=$(git grep -l "ground-x") && echo $files | xargs -t sed -i 's/ground-x/klaytn/g'
