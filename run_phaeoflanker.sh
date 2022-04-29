#!/bin/bash

#SBATCH --mem 10GB 
#SBATCH -o phaeoflanker.%N.%j.out
#SBATCH -e phaeoflanker.%N.%j.err
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=pjacques@sb-roscoff.fr
#SBATCH -p fast

#module load bedtools

cntig_file='contigs/contig_summary.tsv'
fasta_fold='../sources_fa'
saves_fold='../sources_EVEs'
cotxt_qual='hvh'

python3 pycode/extractEVEsData.py $cntig_file $fasta_fold $saves_fold $cotxt_qual

