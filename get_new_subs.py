## Get all subjects, sessions available in dicoms folder
## Check if theyve already been converted to BIDS
## if any modality is missing, the whole dir can be rerun 
import pandas as pd
import os
import csv

# CSV dir and name, how to save the resulting CSV
csv_dir = os.getcwd()
csv_filename = os.path.join(csv_dir,'newsubs.csv')

# bids dir to check inside
bids_dir = '/working/mochila2/JC/data/bids'

def check_for_bids(combo):
    func_dir =  os.path.join(bids_dir,'sub-'+combo[1], 'ses-'+combo[2],'func') 
    fmap_dir  = os.path.join(bids_dir,'sub-'+combo[1], 'ses-'+combo[2],'fmap')
    anat_dir  = os.path.join(bids_dir,'sub-'+combo[1], 'ses-'+combo[2],'anat')
    return all([os.path.exists(func_dir), os.path.exists(fmap_dir), os.path.exists(anat_dir)])


#read in CSV list of all brain dirs
newsubs = []
with open('input_dcm2bids.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if not check_for_bids(row):
            newsubs.append(row)

df = pd.DataFrame(newsubs)
print('Saving CSV at '+csv_filename) 
df.to_csv(csv_filename,header=False,index=False)