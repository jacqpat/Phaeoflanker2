#!/bin/bash

file_ctg=$1
fold_fst=$2
fold_gff=$3
fold_svd=$4
fold_bed=$5
qual_ctx=$6
size_flk=$7
fold_svd_img=$8
fold_svd_gff=$9
fold_svd_fa=${10}
file_svd="${fold_svd}/eves_${qual_ctx}.csv"
bed_file='${fold_bed}/bedfile_${fold_svd_gff}.bed'

python3 pycode/checks_folders.py $fold_svd $fold_bed $fold_svd_img $fold_svd_gff $fold_svd_fa
python3 pycode/extractEVEsData.py $file_ctg $fold_fst $fold_svd $qual_ctx
python3 pycode/extractGenesOfEVEs.py $file_svd $fold_gff $size_flk $fold_svd_gff $fold_bed

eves=$(cat ${file_svd} | cut -d \, -f 2)
a_eves=()
a_srcs=()
for e in $eves
do
    a_eves+=($e)
done
a_eves=("${a_eves[@]:1}")
srcs=$(cat ${file_svd} | cut -d \, -f 6)
for s in $srcs
do
    a_srcs+=($s)
done
a_srcs=("${a_srcs[@]:1}")

for i in "${!a_eves[@]}"
do
    sc="${fold_fst}/${a_srcs[$i]}"
    ev="${fold_svd_gff}/EVE_${a_eves[$i]}.gff"
    up="${fold_svd_gff}/EVE_${a_eves[$i]}_up.gff"
    dw="${fold_svd_gff}/EVE_${a_eves[$i]}_down.gff"
    fev="${fold_svd_fa}/EVE_${a_eves[$i]}.fa"
    fup="${fold_svd_fa}/EVE_${a_eves[$i]}_up.fa"
    fdw="${fold_svd_fa}/EVE_${a_eves[$i]}_down.fa"
    bev="${fold_bed}/${a_eves[$i]}_eve.bed"
    bup="${fold_bed}/${a_eves[$i]}_up.bed"
    bdw="${fold_bed}/${a_eves[$i]}_down.bed"
    python3 pycode/drawEVE.py $ev $fold_svd_img
    python3 pycode/drawEVE.py $up $fold_svd_img
    python3 pycode/drawEVE.py $dw $fold_svd_img
    if [ -f "$bev" ]; then
        bedtools getfasta -fi $sc -bed $bev -fo $fev
    fi
    if [ -f "$bup" ]; then
        bedtools getfasta -fi $sc -bed $bup -fo $fup
    fi
    if [ -f "$bdw" ]; then
        bedtools getfasta -fi $sc -bed $bdw -fo $fdw
    fi
done
