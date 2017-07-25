f = open('sequence.protein.2.fasta', 'r')

l = f.xreadlines()

line = l.readline()
line = l.readline().rstrip()

print 'The second line is: ' + line
