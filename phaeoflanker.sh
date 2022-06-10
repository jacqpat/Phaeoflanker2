#!/bin/bash

#SBATCH --mem 10GB 
#SBATCH -o phaeoflanker.%N.%j.out
#SBATCH -e phaeoflanker.%N.%j.err
#SBATCH --cpus-per-task=1
#SBATCH -p fast

#module load bedtools

file_ctg='path/to/summary_file.tsv' # <= tsv or csv
fold_fst='path/to/fasta/folder'
fold_gff='path/to/gff/folder'
fold_svd='../sources_EVEs' # <= change to where you want to stock intermediate files
fold_bed='../BED' # <= change to where you want to stock BED files
qual_ctx='v' # <= hvh / vh / v depending on what kind of EVEs you want
size_flk="100000" # <= number of bp
fold_svd_img="../eves_and_flanks_img" # <= change to where you want to stock final images
fold_svd_gff="../eves_and_flanks_gff" # <= change to where you want to stock extracted gff
fold_svd_faa="../eves_and_flanks_fa" # <= change to where you want to stock extracted fasta

./shcode/pf_inner_script.sh $file_ctg $fold_fst $fold_gff $fold_svd $fold_bed $qual_ctx $size_flk $fold_svd_img $fold_svd_gff $fold_svd_faa
