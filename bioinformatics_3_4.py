f1 = open('sequence.fasta', 'r')
f2 = open('sequence.protein.2.fasta', 'w')

f2.write(f1.read())
