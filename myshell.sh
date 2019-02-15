#!/bin/sh
ans=$(python first_borda.py | sort -k1,1 | python reducer.py |sort -k2,2nr -k2,2|head -50 | cat $1 > output.csv)
echo $ans
