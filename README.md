# Phaeoflanker2
new version of Phaeoflanker pipeline
# To start with Phaeoflanker
The first step is to prepare a tsv or csv file containing the list of contigs/chromosomes/sequences where there are known EVEs. There must be the following column, with these exact names : 'contig','EVE_start','EVE_end','context'. You can add as many other column you want in any order, but as of version 1.0 these columns are mandatory. You can then add this file to the 'contig' folder.

You fasta and gff files can be storaged anywhere you want as long as they are accessible to Phaeoflanker and in separate folders. Change their respective path in the bash file.

You can now launch the bash file from your console.
