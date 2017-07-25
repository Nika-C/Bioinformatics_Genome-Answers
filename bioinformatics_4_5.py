F = open('sequence.nucleotide.gb', 'r')

Line = F.xreadlines()

seq = ''
first = True
for l in Line:
    if 'TITLE' in l and first == True:
        first = False
        seq += l
    elif 'TITLE' in l:
        seq += l.replace('TITLE', '     ')

print seq

