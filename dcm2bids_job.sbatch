#!/bin/bash
#SBATCH --job-name=dcm2bids
#SBATCH  output=/working/mochila2/JC/code/make-bids/logs/%x-%j.log

pwd; hostname; date

eval "$('/netopt/rhel7/versions/python/Anaconda3-edge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"

# enter location of dcm2bids conda environment
conda activate /working/mochila2/JC/conda/envs/dcm2bids

# enter location of bids dir (where you want output) and config json file 
bids_dir=/working/mochila2/JC/data/bids
config_file=/working/mochila2/JC/data/bids/code/config_updated.json

echo "Running dcm2bids for BACPAC sub-${1}."

# Initial run: won't replace files or rerun if already run/cached:
#dcm2bids -o $bids_dir -d $1 -p $2 -s $3 -c $config_file

# For running on new subs or re-running with new configuration:
dcm2bids -o $bids_dir -d $1 -p $2 -s $3 -c $config_file --forceDcm2niix --clobber