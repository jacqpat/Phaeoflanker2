#!/bin/bash

#SBATCH --mem 10GB 
#SBATCH -o phaeoflanker.%N.%j.out
#SBATCH -e phaeoflanker.%N.%j.err
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=pjacques@sb-roscoff.fr
#SBATCH -p fast

#module load bedtools

file_ctg='contigs/contig_summary.tsv'
fold_fst='../sources_fa'
fold_gff='../sources_gff'
fold_svd='../sources_EVEs'
qual_ctx='hvh'
file_svd="${fold_svd}/eves_${qual_ctx}.csv"
size_flk="100000"
fold_svd_gff="../eves_and_flanks_gff"

python3 pycode/extractEVEsData.py $file_ctg $fold_fst $fold_svd $qual_ctx
python3 pycode/extractGenesOfEVEs.py $file_svd $fold_gff $size_flk $fold_svd_gff