#!/bin/bash

# Clean up the files that this generates
rm *.cinject
rm main.*

# Run the preprocessor to create the .cinject files
# and get the curent year from the user
python3.11 preprocessor.py

# Concatenate all of the partial C source files into main.c
cat main0.cstub >  main.c
cat preprocessed0.cinject >> main.c
cat main1.cstub >> main.c
cat preprocessed1.cinject >> main.c
cat main2.cstub >> main.c

# Compile the newly generated main.c into main.out
gcc main.c -o main.out

# Run main.out
./main.out
