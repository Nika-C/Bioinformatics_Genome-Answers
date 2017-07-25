
f = open('sequence.protein.gb', 'r')

l = f.xreadlines()
title = l.readline()

for i in l:
    lines = i.rstrip()
    if lines[0:7] == 'ORIGIN':
        break

seq = ''
for i in l:
    seq += i

print 'seq: ' + seq

