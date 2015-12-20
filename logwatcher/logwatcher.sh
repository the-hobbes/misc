#!/bin/bash

# touch logfile.log
# ./logwatcher.sh
# echo "something" >> logfile.log
# echo "somestring" >> logfile.log 

tail -f logfile.log | while read LOGLINE
do
   [[ "${LOGLINE}" == *"somestring"* ]] && echo "I've found the string!"
done
