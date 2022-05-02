'''
Written by Patrick Jacques the 29th of April 2022

from informations about the EVEs, create BED files
useable by BEDTools

python3 getEVEs_sequences.py [BED SAVE FOLDER] [GFF FOLDER]
'''
import os
import sys
import time
import common_code as cc
from class_gff import Gene

folder_bed = sys.argv[1]
folder_gff = sys.argv[2]
cc.check_and_make(folder_bed)

bbstring = ''
for filename in os.listdir(folder_gff):
    f = os.path.join(folder_gff, filename)
    if os.path.isfile(f) and filename[-3:] == 'gff':
        basef = os.path.basename(f[:-4])
        gff_lines = cc.get_lines(f)
        start = -1
        end = -1
        for x in gff_lines:
            x = x.rstrip('\n')
            x = x.split('\t')
            g = Gene(x)
            if start == -1:
                start = g.start
            else:
                if g.start < start:
                    start = g.start
            if end == -1:
                end = g.end
            else:
                if g.end > end:
                    end = g.end
        bstring = f'{basef}\t{start}\t{end}\n'
        bbstring += bstring
nb = 0
bbstring = bbstring.rstrip('\n')
path2file = f'bedfile{nb}.bed'
while path2file in os.listdir(folder_bed):
    nb += 1
    path2file = f'bedfile{nb}.bed'
path2file = os.path.join(folder_bed, path2file)
cc.save_file(path2file,bbstring)