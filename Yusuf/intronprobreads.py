import sys
import gzip

filepath = sys.argv[1]

def counttotal():
    total_reads = 0
    with gzip.open(filepath, 'rt') as fp:
        for line in fp:
            if line.startswith('#'): continue
            cols = line.split()
            print(cols[1])
            if cols[1] == 'RNASeq_splice' and cols[2] == 'intron':
                total_reads += int(float((cols[5])))
        return total_reads
print(counttotal())

def prob_intron(start, end, strand): 
    with gzip.open(filepath, 'rt') as fp:
        for line in fp:
            cols = line.split()
            if line.startswith('#'): continue
            if int(cols[3]) == start and int(cols[4]) == end and cols[6] == strand:
                seqprob = int(float((cols[5]))) / counttotal()
        return seqprob
                
            
print(prob_intron(3258, 3504, '-'))
