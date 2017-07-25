#import dictionary for codon
import CodonDict
Dict = CodonDict.CodonDict()

#read sequence from file
Seq = ''
with open('sequence.nucleotide.fasta', 'r') as Line:
    Line.readline()
    for l in Line:
        Seq += l.rstrip()

#convert sequence into a list of Codons
List = []
Codon = ''
for i in Seq:
    Codon += i
    if len(Codon) == 3:
        List.append(Codon)
        Codon = ''

#convert codon list into amino acid
AA = []
for i in List:
    aa = Dict[i]
    AA.append(aa)

seq_aa = '  '.join(AA)
seq_aa += '  '

#format DNA & AA sequence and print
c = 0
Line_dna = ''
Line_aa = ''
for i in Seq:
    Line_dna += Seq[c]
    Line_aa += seq_aa[c]
    c += 1

    if c%60 == 0 or c == len(Seq):
        print Line_dna
        print Line_aa
        Line_dna = ''
        Line_aa = ''

