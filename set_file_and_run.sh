#!/bin/bash

#SBATCH --mem 10GB 
#SBATCH -o phaeoflanker.%N.%j.out
#SBATCH -e phaeoflanker.%N.%j.err
#SBATCH --cpus-per-task=1
#SBATCH -p fast

#module load bedtools

file_ctg='contigs/contig_summary.tsv'
fold_fst='../sources_fa'
fold_gff='../sources_gff'
fold_svd='../sources_EVEs'
fold_bed='../BED'
qual_ctx='hvh'
size_flk="100000"
fold_svd_img="../eves_and_flanks_img"
fold_svd_gff="../eves_and_flanks_gff"
fold_svd_faa="../eves_and_flanks_fa"

./shcode/phaeoflanker.sh $file_ctg $fold_fst $fold_gff $fold_svd $fold_bed $qual_ctx $size_flk $fold_svd_img $fold_svd_gff $fold_svd_faa