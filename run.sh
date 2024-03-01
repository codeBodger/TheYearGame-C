#!/bin/bash

# Clean up the files that this generates
rm *.cinject
rm main.*

python3.11 preprocessor.py

cat main0.cstub >  main.c
cat preprocessed0.cinject >> main.c
cat main1.cstub >> main.c
cat preprocessed1.cinject >> main.c
cat main2.cstub >> main.c

gcc main.c -o main.out

./main.out
