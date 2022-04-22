'''
Written by Patrick Jacques the 22th April 2022

Script to parse the contigs summary ods file Dean left us
'''
import pandas as pd
import common_code as cc

df1 = cc.read_tsv_file()
df2 = df1.filter(['contig','EVE_start','EVE_end','context'], axis=1)
print(df2)