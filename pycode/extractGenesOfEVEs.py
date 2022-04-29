'''
Written by Patrick Jacques the 29th of April 2022

Now that we have the localisation and tags of all the eves we want,
we can get all of their genes
'''
import os
import sys
import time
import pandas as pd
import common_code as cc
from class_gff import Gene

def save_as_gff(dict,path):
    for k,v in dict.items():
        filepath = f'{path}/EVE_{k}.gff'
        bbstring = ''
        for i in v:
            bbstring += f'{i.get_gff_line()}\n'
        bbstring = bbstring.rstrip('\n')
        cc.save_file(filepath,bbstring)

t_start = time.process_time()
file_eve = sys.argv[1]
fold_gff = sys.argv[2]
flk_size = int(sys.argv[3])
gff_safe = sys.argv[4]

df_eves = cc.read_csv_file(path = file_eve)
seqs_eves = df_eves['contig'].tolist()

eves_genes = {}
flanks_genes = {}
for filename in os.listdir(fold_gff):
    f = os.path.join(fold_gff, filename)
    if os.path.isfile(f) and filename[-3:] == 'gff':
        gff_lines = cc.get_lines(f)
        for x in gff_lines:
            x = x.rstrip('\n')
            x = x.split('\t')
            if len(x) == 9 and x[0] in seqs_eves:
                g = Gene(x)
                b = int(df_eves.loc[df_eves['contig'] == g.sequence,'EVE_start'])
                e = int(df_eves.loc[df_eves['contig'] == g.sequence,'EVE_end'])
                if (g.start >= b and g.start <= e) or (g.end >= b and g.end <= e):
                    if g.sequence in eves_genes:
                        eves_genes[g.sequence].append(g)
                    else:
                        eves_genes[g.sequence] = [g]
                elif (g.start < b and g.end < b) and (g.start >= b-flk_size and g.end >= b-flk_size):
                    if f'{g.sequence}_up' in flanks_genes:
                        flanks_genes[f'{g.sequence}_up'].append(g)
                    else:
                        flanks_genes[f'{g.sequence}_up'] = [g]
                elif (g.start > e and g.end > e) and (g.start <= e+flk_size and g.end <= e+flk_size):
                    if f'{g.sequence}_down' in flanks_genes:
                        flanks_genes[f'{g.sequence}_down'].append(g)
                    else:
                        flanks_genes[f'{g.sequence}_down'] = [g]

cc.check_and_make(gff_safe)
save_as_gff(eves_genes,gff_safe)
save_as_gff(flanks_genes,gff_safe)

print(time.process_time() - t_start)