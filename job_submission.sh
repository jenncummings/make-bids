#!/bin/bash

INPUT=newsubs.csv
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read dir subject session
do
    #echo "dir : $dir"
    #echo "subject : $subject"
    #echo "session : $session"
    #sh job_test.sh $dir $subject $session
    sbatch dcm2bids_job.sbatch $dir $subject $session
done < $INPUT
IFS=$OLDIFS
