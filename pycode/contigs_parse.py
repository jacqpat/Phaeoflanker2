'''
Written by Patrick Jacques the 22th April 2022

Script to parse the contigs summary ods file Dean left us
'''
import sys
import pandas as pd
import common_code as cc

df1 = cc.read_tsv_file()
df2 = df1.filter(['contig','EVE_start','EVE_end','context'], axis=1)
try:
    df_HVH = df2[df2.context == 'HVH']
    df_HV = df2[df2.context == "HV"]
    df_V = df2[df2.context == "V"]
except AttributeError:
    print('csv given with wrong headers')
    sys.exit()
print(df2)