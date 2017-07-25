import re
p = re.compile('[A-Z]+')
L = ''
check = 0
c = 0
Seq = ''
Seq_f = ''

#find appropriate section
with open('sequence.nucleotide.gb', 'r') as fr:
    for l in fr:
        if l.strip().startswith('/translation'):
            check = 1
        if l.strip().startswith('STS'):
            check = 0

        if check == 1:
            L += l.strip()

#string lines into only the codes
for i in p.findall(L):
    Seq += i
Seq += '*'

#format sequence to print 70 characters per line
for i in Seq:
    c += 1
    Seq_f += i
    if c % 70 == 0:
        Seq_f += '\n'

print Seq_f
