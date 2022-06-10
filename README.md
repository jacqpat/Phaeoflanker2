# Phaeoflanker2
new version of Phaeoflanker pipeline

<img src="https://i.imgur.com/6ICdkFr.png" width="750">

# To start with Phaeoflanker
Phaeoflanker 2 is meant to be useable both on your personal computer and on a remote server. As such, all the parameters needed for this script can be found and modified in the 'set_and_run.sh' file. It is the only file you will have to interact with to run Phaeoflanker.

Phaeoflanker 2 has only one dependency : **Bedtools**. Make sure it is present on the computer or server you're using beforehand.

Then, prepare a tsv or csv file following the example given in the 'contig' folder of this repository. The columns  'contig','EVE_start','EVE_end', and 'context' are mandatory, with these exact names.

Your fasta and gff files can be storaged anywhere you want as long as they are accessible to Phaeoflanker and in separate folders.

Once you have prepared all your files and repositories, go to 'set_and_run.sh' and modify the paths to reach all of these files. The variables you can change are :

1) *file_ctg* : path to the csv or tsv format you have prepared.
2) *fold_fst* : path to the folder where you've stored your fasta files.
3) *fold_gff* : path to the folder where you've stored your gff files.
4) *fold_svd* : path to the folder where you want to save the intermediary csv file resuming all your EVEs.
5) *fold_bed* : path to the folder where you want to save the intermediary BED file.
6) *qual_ctx* : the quality of the contigs you want to keep. See below for a detailed description.
7) *size_flk* : the maximum size of the flanking regions you want to keep.
8) *fold_svd_img* : path to the folder where you want to save all the images generated by Phaeoflanker.
9) *fold_svd_gff* : path to the folder where you want to save all the gff files generated by Phaeoflanker.
10) *fold_svd_faa* : path to the folder where you want to save all the fasta files generated by Phaeoflanker.

Once you've set the variables, you can launch set_and_run.sh from your console.

# contig quality
Phaeoflanker demand that you associate to your contigs / sequences a quality indicator (the 'context' column in your csv resume). This may change in following version, but currently it work this way :
in the csv/tsv resume, in the column 'context', give each of EVE one of the following indicator :

1) **HVH** : your EVE is flanked on both side by algal genome.
2) **HV** : your EVE is flanked on one side only by algal genome. Do NOT change it to VH if the algal genome is downstream of the EVE. Leave it as HV.
3) **V** : your EVE represent the entirety of the contig. It is impossible to tell if it's an EVE or a Provirus.

You can then extract specifically EVE annoted in one of those three categories by modifying to *qual_ctx* parameter in 'set_and_run.sh'. The accepted variables are the following (upper or lower cases don't matter) :

1) '"good", "g", or "hvh" for the HVH category.
2) "maybe", "m", "hv", or "vh" for the HV category.
3) "provirus", "p", or "v" for the V category.

# Authors
* **Patrick Jacques** _alias_ [@jacqpat](https://github.com/jacqpat)

# License
This project is under GPL-3.0 License - see LICENSE.md file for more information
