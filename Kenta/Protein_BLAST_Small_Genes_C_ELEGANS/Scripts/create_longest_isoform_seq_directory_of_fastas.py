import glob
import threading
import subprocess
import os

# Create output directory if it doesn't exist
output_dir = "/Users/kentahsu/Code/KorfLab/RNA_Seq_Analysis/Kenta/Protein_BLAST_Small_Genes_C_ELEGANS/longest_isoform_entire_CDS_fastas"

fastas = glob.glob("/Users/kentahsu/Code/KorfLab/RNA_Seq_Analysis/Kenta/Refs/smallgenes/*.fa")
gffs = glob.glob("/Users/kentahsu/Code/KorfLab/RNA_Seq_Analysis/Kenta/Refs/smallgenes/*.gff3")

for fasta in fastas:
    for gff in gffs:    
        if fasta.split(".")[1] == gff.split(".")[1]:
            # Get the base name for the output file
            base_name = "ch." + fasta.split(".")[1] + "_longest_isoform.fa"
            # print("this is name: ",base_name)
            output_file = os.path.join(output_dir, base_name)
            #print("this is output file: ", output_file)
            
            # Run subprocess and redirect output to file
            with open(output_file, 'w') as f:
                subprocess.run(["python3", "longest_isoform.py", fasta, gff], stdout=f, text=True, check=True)

