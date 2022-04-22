'''
Written by Patrick Jacques the 22th April 2022

Script to parse the contigs summary ods file Dean left us
'''
import os
import sys
import time
import pandas as pd
import common_code as cc
from gff_parse import Gene
from pathlib import Path

start = time.process_time()
f = sys.argv[1]
fld = sys.argv[2]
gff = sys.argv[3]
ctx = sys.argv[4].lower()

### parsing contig to keep only EVEs or provirus ###

## can take either tsv or csv files ##
if f[-3:] == "tsv":
    df1 = cc.read_tsv_file(path = f)
elif f[-3:] == "csv":
    df1 = cc.read_csv_file(path = f)

## keep only the columns that we want + rows with the demanded context ##
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

## from the fasta folder, keep only the contigs with an EVE and make a new dataframe with them ##
df_ourEVEs = pd.DataFrame(columns= ['contig','EVE_start','EVE_end','context'])
for filename in os.listdir(fld):
    f = os.path.join(fld, filename)
    if os.path.isfile(f) and (f.endswith(".fa") or f.endswith(".fasta")):
        with open(f,'r', encoding = 'utf-8') as fa:
            fa_lines = fa.readlines()
            for l in fa_lines:
                if l.startswith('>'):
                    contig_name = l[1:-1]
                    # without this check, we go from 6 to 41 seconds (with HVH context)
                    if contig_name in df3['contig'].tolist():
                        df_ourEVEs = pd.concat([df_ourEVEs,df3.loc[df3['contig'] == contig_name]])
print(df_ourEVEs)

### parse the gff files ###
eves_genes = {}
for filename in os.listdir(gff):
    eve_gen_list = []
    print(filename[:-4])
    f = os.path.join(gff,filename)
    if os.path.isfile(f) and f.endswith(".gff"):
        with open(f,'r', encoding = 'utf-8') as gf:
            gf_lines = gf.readlines()
            for l in gf_lines:
                l1 = l.rstrip('\n')
                l2 = l1.split('\t')
                if len(l2) == 9:
                    g = Gene(l2)
                    if g.sequence in df_ourEVEs['contig'].tolist():
                        if (int(g.start) >= int(df_ourEVEs.loc[df_ourEVEs['contig'] == g.sequence,'EVE_start']) and int(g.start) <= int(df_ourEVEs.loc[df_ourEVEs['contig'] == g.sequence,'EVE_end']))\
                        or (int(g.end) >= int(df_ourEVEs.loc[df_ourEVEs['contig'] == g.sequence,'EVE_start']) and int(g.end) <= int(df_ourEVEs.loc[df_ourEVEs['contig'] == g.sequence,'EVE_end'])):
                            eve_gen_list.append(g)
    for g in eve_gen_list:
        print(g.attributes.get('ID'))
'''
TODO :
find a way to have :
eves_genes[g.sequence][g]
'''
print(time.process_time() - start)