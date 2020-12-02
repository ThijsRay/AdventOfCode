#!/bin/bash

input=$(cat input.txt)
idx=0

while IFS= read -r line1
do
    idx=$(expr $idx + 1)
    while IFS= read -r line2
    do
        sum=$(expr $line1 + $line2)
        if [ $sum -eq 2020 ]
        then
            echo "$sum = $line1 + $line2"
            result=$(expr $line1 \* $line2)
            echo "$result = $line1 * $line2"
            exit 0
        fi
    done < <(tail -n $idx input.txt)
done < input.txt
exit 1

