#!/bin/bash

python3.11 preprocessing.py

cat main0.cstub >  main.c
cat main1.cstub >> main.c
cat preprocessed.cinject >> main.c
cat main2.cstub >> main.c

gcc main.c -o main.out

./main.out
