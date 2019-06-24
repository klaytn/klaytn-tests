#!/bin/bash

# Description
# This script updates values of "hash" and "logs" in *.json files if `make test` fails.
# This is useful when you change default behaviors of Klaytn.
# 
# How to use
# $ ./update_state.sh

TEE_OUT_FILENAME=tee_output
FILTERED_FILENAME=tee_output_filtered

ADDITIONAL=""
if [ ! -z "$1" ]; then
  ADDITIONAL="-run $1"
fi

pushd ../
go test $ADDITIONAL 2>&1 | tee $TEE_OUT_FILENAME
grep -A1 "        --- FAIL" $TEE_OUT_FILENAME > $FILTERED_FILENAME
rm $TEE_OUT_FILENAME
mv $FILTERED_FILENAME testdata
popd

./apply_failed_state.py $FILTERED_FILENAME
rm -rf $FILTERED_FILENAME
