#!/bin/bash

for i in {2..100}
do
    isprime=1
    sq=$(bc <<< "scale = 0; sqrt($i)")
    for ((j=2; j<=$sq; ++j))
    do
        if [ $((i%j)) -eq 0 ]
        then
            isprime=0
            break
        fi
    done
    if [ $isprime -eq 1 ]
    then
        echo "$i"
    fi
done