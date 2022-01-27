bids_dir=/working/mochila2/JC/dcm2bids_3
config_file=/working/mochila2/JC/dcm2bids_2/config.json

echo dcm2bids -o $bids_dir -d $1 -p $2 -s $3 -c $config_file