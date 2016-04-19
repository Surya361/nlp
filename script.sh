#!/bin/bash
for i in {0..9}
do
python bigramnaive.py $i >> $1
done
