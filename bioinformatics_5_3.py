#dictionaries for translation & complimentary strand
import CodonDict
Dict = CodonDict.CodonDict()
nDic = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

#read sequence from fasta file, get sequence & reverse sequence
Seq = ''
cSeq = ''
with open('sequence.nucleotide.fasta', 'r') as Line:
    for l in Line:
        if l.startswith('>'):
            pass
        else:
            Seq += l.rstrip()

for i in Seq:
    cSeq += nDic[i]
rcSeq = cSeq[::-1]

#function for getting amino acid seq from 3 Codon sets (frame: 1~3, S = Sequence)
def getCodon(frame = 0, S = Seq):
    List = []
    Last = False
    AA = ''
    for i in range(frame,len(S),3):
        try:
            S[i+2]
        except:
            Last = True
            break
        List.append(S[i:i+3])

    for codon in List:
        aa = Dict[codon]
        AA += (' '*frame + aa + ' '*(2-frame))

    if Last == True:
        AA += '   '

    return AA

#print as requested by problem
print getCodon()
print getCodon(frame = 1)
print getCodon(frame = 2)
print Seq
print cSeq
print getCodon(S = rcSeq)[::-1]
print getCodon(frame = 1, S = rcSeq)[::-1]
print getCodon(frame = 2, S = rcSeq)[::-1]

