'''
Written by Patrick Jacques the 22th April 2022

Script to parse the contigs summary ods file Dean left us
'''
import sys
import pandas as pd
import common_code as cc

f = sys.argv[1]
ctx = sys.argv[2]
if f[:-3] == "tsv":
    df1 = cc.read_tsv_file(path = f)
elif f[:-3] == "csv":
    df1 = cc.read_csv_file(path = f)
df2 = df1.filter(['contig','EVE_start','EVE_end','context'], axis=1)
try:
    df_HVH = df2[df2.context == 'HVH']
    df_HV = df2[df2.context == "HV"]
    df_V = df2[df2.context == "V"]
except AttributeError:
    print('file listing EVEs given with wrong headers')
    sys.exit()
