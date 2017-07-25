import re
p = re.compile('[a-z]', re.I)

f = open('sequence.protein.gb', 'r')

l = f.xreadlines()
title = l.readline()

for i in l:
    lines = i.rstrip()
    if lines[0:7] == 'ORIGIN':
        break

seq = ''
List = []
for i in l:
    lines = i.rstrip()
    List += p.findall(lines)

for i in List:
    seq += i

print 'seq: ' + seq


