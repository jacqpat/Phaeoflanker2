'''
Written by Patrick Jacques the 22th April 2022

Script to parse the contigs summary ods file Dean left us
'''
import os
import sys
import time
import pandas as pd
import common_code as cc

start = time.process_time()
f = sys.argv[1]
fld = sys.argv[2]
ctx = sys.argv[3].lower()

if f[-3:] == "tsv":
    df1 = cc.read_tsv_file(path = f)
elif f[-3:] == "csv":
    df1 = cc.read_csv_file(path = f)
df2 = df1.filter(['contig','EVE_start','EVE_end','context'], axis=1)
try:
    if ctx == "good" or ctx == "g" or ctx == "hvh":
        df3 = df2[df2.context == 'HVH']
    elif ctx == "maybe" or ctx == "m" or ctx == "hv" or ctx == "vh":
        df3 = df2[df2.context == "HV"]
    elif ctx == "provirus" or ctx == "p" or ctx == "v":
        df3 = df2[df2.context == "V"]
    else:
        print("wrong parameter given")
        sys.exit()
except AttributeError:
    print('file listing EVEs given with wrong headers')
    sys.exit()
df_ourEVEs = pd.DataFrame(columns= ['contig','EVE_start','EVE_end','context'])
for filename in os.listdir(fld):
    f = os.path.join(fld, filename)
    if os.path.isfile(f) and (f.endswith(".fa") or f.endswith(".fasta")):
        with open(f,'r', encoding = 'utf-8') as fa:
            fa_lines = fa.readlines()
            for l in fa_lines:
                if l.startswith('>'):
                    contig_name = l[1:-1]
                    # without this loop, we go from 6 to 41 seconds
                    if contig_name in df3['contig'].tolist():
                        df_ourEVEs = pd.concat([df_ourEVEs,df3.loc[df3['contig'] == contig_name]])
print(df_ourEVEs)
print(time.process_time() - start)