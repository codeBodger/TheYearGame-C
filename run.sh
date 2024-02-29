#!/bin/bash

python3.11 preprocessing.py

cat main.cstub > main.c

gcc main.c -o main.out

./main.out
