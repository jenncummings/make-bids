#!/bin/bash
eval "$('/netopt/rhel7/versions/python/Anaconda3-edge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"

# enter location of dcm2bids conda environment
conda activate /data/rajlab1/user_data/jenn/conda/envs/dcm2bids

# enter location of bids dir (where you want output) and config json file 
bids_dir=/working/mochila2/JC/data/bids
config_file=/working/mochila2/JC/data/bids/code/config.json

dcm2bids -o $bids_dir -d $1 -p $2 -s $3 -c $config_file