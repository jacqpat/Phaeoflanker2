'''
Written by Patrick Jacques the 22th April 2022

Script to parse the contigs summary ods file Dean left us

python3 contigs_parse.py [path_to_contigs_summary] [path_to_fasta_folder] [path_to_save_folder] [hvh/hv/v]
'''
import os
import sys
import time
import pandas as pd
import common_code as cc
from pathlib import Path

start = time.process_time()
f = sys.argv[1]
fld = sys.argv[2]
sfe = sys.argv[3]
ctx = sys.argv[4].lower()

cc.check_and_make(sfe)

### parsing contig to keep only EVEs or provirus ###

## can take either tsv or csv files ##
if f[-3:] == "tsv":
    df1 = cc.read_tsv_file(path = f)
elif f[-3:] == "csv":
    df1 = cc.read_csv_file(path = f)

## keep only the columns that we want + rows with the demanded context ##
df1 = df1.filter(['contig','EVE_start','EVE_end','context'], axis=1)
try:
    if ctx == "good" or ctx == "g" or ctx == "hvh":
        df1 = df1[df1.context == 'HVH']
    elif ctx == "maybe" or ctx == "m" or ctx == "hv" or ctx == "vh":
        df1 = df1[df1.context == "HV"]
    elif ctx == "provirus" or ctx == "p" or ctx == "v":
        df1 = df1[df1.context == "V"]
    else:
        print("wrong parameter given")
        sys.exit()
except AttributeError:
    print('file listing EVEs given with wrong headers')
    sys.exit()

## from the fasta folder, keep only the contigs with an EVE and make a new dataframe with them ##
df_ourEVEs = pd.DataFrame(columns= ['contig','EVE_start','EVE_end','context'])
filenames = []
for filename in os.listdir(fld):
    f = os.path.join(fld, filename)
    if os.path.isfile(f) and (f.endswith(".fa") or f.endswith(".fasta")):
        with open(f,'r', encoding = 'utf-8') as fa:
            fa_lines = fa.readlines()
            for l in fa_lines:
                if l.startswith('>'):
                    contig_name = l[1:-1]
                    # without this check, we go from 6 to 41 seconds (with HVH context)
                    if contig_name in df1['contig'].tolist():
                        df_ourEVEs = pd.concat([df_ourEVEs,df1.loc[df1['contig'] == contig_name]])
                        filenames.append(filename)
df_ourEVEs['og_file'] = filenames
savepath = Path(os.path.join(sfe, f'eves_{ctx}.csv'))
savepath.parent.mkdir(parents=True, exist_ok=True)  
df_ourEVEs.to_csv(savepath) 
print(time.process_time() - start)