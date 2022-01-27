# input = root dir, where all subjects are
# output = csv with entries for path to the "brain" dir, sub ID, sess ID

#%% Imports
import os
import fnmatch
import glob
import pandas as pd

#%%
# Root dir, where to start looking 
root_dir = '/data/mochila1/PatientStudy/UCSF/'

# CSV dir and name, how to save the resulting CSV
csv_dir = os.getcwd()
csv_filename = os.path.join(csv_dir,'input_dcm2bids.csv')

#%% Functions for getting sub and sess info from directory path
def get_patientid_from_path(series_path):
    parts = series_path.split(os.sep)
    for p in parts:
        if fnmatch.fnmatch(p.lower(),'bacpac*'):
            patientid = p[6:]
    return patientid

def get_session_number(series_path):
    parts = series_path.split(os.sep)
    for ix,p in enumerate(parts):
        if fnmatch.fnmatch(p.lower(),'bacpac*'):
            series_folder = parts[ix+1]
    
    sess_num = series_folder[0:2]
    return sess_num

#%% Get all dirs in root dir that have "brain" subdirectory
brain_list = glob.glob(root_dir+"/**/**/brain/")

# Get sub,sess info from dirs
sub_list = []
sess_list = []

for dir in brain_list:
    sub_list.append(get_patientid_from_path(dir))
    sess_list.append(get_session_number(dir))

dict = {'dir': brain_list, 'subject': sub_list, 'session': sess_list}
df = pd.DataFrame(dict) 

print('Saving CSV at '+csv_filename) 
# saving the dataframe 
df.to_csv(csv_filename,header=False,index=False)