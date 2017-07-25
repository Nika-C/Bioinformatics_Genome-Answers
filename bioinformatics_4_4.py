#-*- coding: utf-8 -*-

#user prompt
IF = raw_input('Enter input file: ')
OF = raw_input('Enter output file: ')

Options = '''
Option-1) Read a FASTA format DNA sequence file and make a reverse sequence file.\n
Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file. \n
Option-3) Convert GenBank format file to FASTA format file.'''
print Options

Op = input('Select the option: ')

#open file and retrieve info according to selected option (1-3)
FR = open(IF, 'r')
L = FR.xreadlines()
title = L.readline()
seq = ''
seq_r = ''
seq_f = ''

if Op == 1 or Op == 2:
    for i in L:
        seq += i.rstrip()
        seq_r = seq[::-1]
        seq_f = seq_r

    if Op == 2:
        seq_f = ''
        rDict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        for i in seq_r:
            seq_f += rDict[i]

elif Op == 3:
    import re
    p = re.compile('[a-z]', re.I)
    List = []
    for i in L:
        lines = i.rstrip()
        if lines[0:7] == 'ORIGIN':
            break
    for i in L:
        lines = i.rstrip()
        List += p.findall(lines)
    for i in List:
        seq_f += i

else:
    print 'Select from Option 1~3\n'
    FR.close()
    exit()

FR.close()

#format result into 70 characters per line
seq_fin = ''
c = 0
for i in seq_f:
    seq_fin += i
    c += 1
    if c%70 == 0:
        seq_fin += '\n'
seq_fin += '\n'

#create file
FW = open(OF, 'w')
FW.write(title + seq_fin)
FW.close()
