#!/bin/bash

cat main.cstub > main.c

gcc main.c -o main.out

./main.out
