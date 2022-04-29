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
gff_fold='../sources_gff'
saves_fold='../sources_EVEs'
cotxt_qual='hvh'
saves_file="${saves_fold}/eves_${cotxt_qual}.csv"
flank_size="100000"
gff_saves_fold="../eves_and_flanks_gff"

python3 pycode/extractEVEsData.py $cntig_file $fasta_fold $saves_fold $cotxt_qual
python3 pycode/extractGenesOfEVEs.py $saves_file $gff_fold $flank_size $gff_saves_fold