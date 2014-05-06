#!/bin/bash

for i in {0..200..30}
do
    python analysis.py $i $(expr $i + 30)
done