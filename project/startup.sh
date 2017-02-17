#!/bin/bash

echo $PWD

trap 'kill -TERM $PID' TERM
python project/main.py &
PID=$!
wait $PID
wait $PID
EXIT_STATUS=$?
