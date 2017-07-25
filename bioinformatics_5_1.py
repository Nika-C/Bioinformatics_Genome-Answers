Codon = ''
c = 0
Seq = ''

with open('sequence.nucleotide.fasta', 'r') as Line:
    Line.readline()
    for l in Line:
        Seq += l.rstrip()

Codon = ''
List = []
for i in Seq:
    Codon += i
    if len(Codon) == 3:
        List.append(Codon)
        Codon = ''

for i in List:
    if len(i) == 3:
        print i
