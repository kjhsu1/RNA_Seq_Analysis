# This script is used to get the longest isoform from a gff file and return the fasta sequence of the longest isoform

import sys

fasta = sys.argv[1] 
gff = sys.argv[2]

# get the longest isoform from a gff file
# return the name of the longest isoform
def get_longest_isoform(gff):
	isoform_dict = {}
	with open(gff, "r") as file:
		for line in file:
			cols = line.split()
			if len(cols) < 9: break
			if (cols[1], cols[2]) != ("WormBase", "CDS"): continue
			tags = cols[8].split(";")
			for tag in tags:
				if tag.startswith("Parent=Transcript") == False: continue
				if tag not in isoform_dict:
					isoform_dict[tag] = 0
				isoform_dict[tag] = isoform_dict[tag] + (int(cols[4]) - int(cols[3])) # add the length of the CDS
	# find longest isoform
	longest_isoform = max(isoform_dict, key=isoform_dict.get)

	return longest_isoform

# print(f"The longest isoform is {get_longest_isoform(gff)}")

# get the longest isoform fasta sequence 
# return the sequence of the longest isoform
def get_longest_isoform_fasta(fasta, longest_isoform):
	coordinates = []  # initialize list to store coordinate tuples
	with open(gff, "r") as file:
		for line in file:
			cols = line.split()
			if (cols[1], cols[2]) != ("WormBase", "CDS"): continue
			tags = cols[8].split(";")
			if longest_isoform in tags:
				coordinates.append((int(cols[3]), int(cols[4])))  # store start and end coordinates as tuple

	# sort coordinates by start position
	# sometimes the coordinates are not in order in the gff file
	coordinates.sort(key=lambda x: x[0])

	# piece together the entire cds sequence
	entire_cds = ""
	full_seq = ""
	with open(fasta, "r") as file:
		# for some reason, the fasta seq is not in one single line
		# so we need to concatenate them firs
		for line in file:
			if line.startswith(">"): continue
			full_seq += line.strip()
		
		for start, end in coordinates:
			cds = full_seq[start-1:end]
			entire_cds += cds
	return entire_cds

print(f">{get_longest_isoform(gff)}")
print(get_longest_isoform_fasta(fasta, get_longest_isoform(gff)))










