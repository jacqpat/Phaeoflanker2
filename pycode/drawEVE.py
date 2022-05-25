'''
Written by Patrick Jacques the 20th of May 2022

Modification of a previous script to isolate just
the drawing of a gff sequence

python3 drawEVE.py [GFF FILE] [SAVE FILE]
'''
import os
import sys
from pyx import *
from class_gff import Gene
import common_code as cc

def draw_sequence_svg(widths,values,bname):
    c = canvas.canvas()
    back_pos = 0
    height = min(widths)
    for i in range(len(widths)):
        width = widths[i]
        if values[i] == 'mRNA_cellular':
            c.fill(path.rect(back_pos, 0, width, height), [color.rgb.green])
        elif values[i] == 'mRNA_viral':
            c.fill(path.rect(back_pos, 0, width, height), [color.rgb(0.5,0,0)])
        elif values[i] == 'mRNA_cellular_or_viral':
            c.fill(path.rect(back_pos, 0, width, height), [color.rgb(0.8,0.5,0)])
        else:
            c.fill(path.rect(back_pos, 0, width, height), [color.gray(0.8)])
        back_pos = back_pos + widths[i]
    c.writeSVGfile(bname)
    print(f'{bs_name} drawn')

seq_des_gff = sys.argv[1]
savefile = sys.argv[2]
cc.check_and_make(savefile)
bs_name = str(savefile + '/' + os.path.basename(seq_des_gff))
lines = cc.get_lines(seq_des_gff)
goi = {}
for x in lines:
        x = cc.rstrip_and_split(x)
        g = Gene(x)
        try:
            goi[g.attributes['ID']] = g
        except KeyError:
            continue
g_width = []
g_value = []
for k,v in goi.items():
    g_width.append(v.taille()/100)
    g_value.append(v.element)
if g_width :
    draw_sequence_svg(g_width,g_value,bs_name)