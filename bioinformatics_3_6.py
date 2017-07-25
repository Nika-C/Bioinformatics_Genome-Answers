f = open('sequence.protein.2.fasta', 'r')

l = f.xreadlines()

title = l.readline().rstrip()

seq = ''
for i in l:
    li = i.rstrip()
    seq = seq + li

print 'title: ' + title
print 'seq: ' + seq
