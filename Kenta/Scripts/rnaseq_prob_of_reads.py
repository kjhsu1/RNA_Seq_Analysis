import gzip
import sys

# calculate prob. of observing intron in a RNAseq exp.
# user needs to give three values
	# chrom, start, stop, and +/- strand

gff = sys.argv[1] # gff file path

def total_reads(gff):
	features = []
	read_sum = 0
	with gzip.open(gff, 'rt') as file:
		for line in file:
			if line.startswith('#'): 
				continue
			words = line.split()
			feature = words[1]
			if feature == 'RNASeq_splice':
				read_sum += int(float(words[5]))
	return read_sum

def prob_read(gff, chrom, start, end, strand):
	total = total_reads(gff)
	# gff is sorted from beginning to end
		# can use binary search?
	with gzip.open(gff, 'rt') as file:
		num_reads = 0
		for line in file:
			words = line.split()
			if line.startswith('#'):
				continue
			if (words[0], words[1], words[2], int(words[3]), int(words[4]), words[6]) == (chrom, 'RNASeq_splice', 'intron', start, end, strand):
				num_reads = int(words[5])
				# Issue: when trying to print(line) the + and . seems to be
				# missing, but line.split()[6] will print '-' which is weird
				# print(line)
				break

	return num_reads/total

print(f"Total # of Intron RNA Seq Reads: {total_reads(gff):g}")
print(f"Probability of Your Intron is {prob_read(gff, 'I', 3258, 3504, '-')}")

'''
count = 0
with gzip.open(gff, 'rt') as file:
	for line in file:
		if count == 5: break
		if line.startswith('#'):
			continue
		words = line.split()
		if words[1] == 'RNASeq_splice':
			print(line)
			count += 1
'''

'''
with gzip.open(gff, 'rt') as file:
	for line in file:
		print(line)
'''


