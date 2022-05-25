'''
Written by Patrick Jacques the 29th of April 2022

Now that we have the localisation and tags of all the eves we want,
we can get all of their genes

May 26th 2022 : merged with getBED_of_EVE.py as it was still actually the
                simplest way to get the job done.

python3 extractGenesOfEVEs.py [ABSTRACT_OF_EVEs] [GFF_FOLDER] [SIZE_FLANK] [GFF SAVE FOLDER] [BED SAVE FOLDER]
'''
import os
import sys
import time
import pandas as pd
import common_code as cc
from class_gff import Gene

def save_as_bed(dict,path):
    for y,v in dict.items():
        t = ''
        k = y
        if '_down' in k:
            t = 'down'
            k = k.rstrip('_down')
        elif '_up' in k:
            t ='up'
            k = k.rstrip('_up')
        else:
            t = 'eve'
        start = -1
        end = -1
        for i in v:
            if start == -1:
                start = i.start
            else:
                if i.start < start:
                    start = i.start
            if end == -1:
                end = i.end
            else:
                if i.end < end:
                    end = i.end
        bbstring = f'{k}\t{start}\t{end}'
        filepath = f'{path}/{t}_{k}.bed'
        cc.save_file(filepath,bbstring)
        print(f'{filepath} printed')

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
folder_bed = sys.argv[5]

df_eves = cc.read_csv_file(path = file_eve)
seqs_eves = df_eves['contig'].tolist()

eves_genes = {}
flanks_genes = {}
'''
make the gff
'''
for filename in os.listdir(fold_gff):
    f = os.path.join(fold_gff, filename)
    f2 = os.path.splitext(f)
    if os.path.isfile(f) and f2[1] == '.gff':
        gff_lines = cc.get_lines(f)
        for x in gff_lines:
            x = cc.rstrip_and_split(x)
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
'''
make the bed
'''
cc.check_and_make(folder_bed)
save_as_bed(eves_genes,folder_bed)
save_as_bed(flanks_genes,gff_safe)

print(time.process_time() - t_start)