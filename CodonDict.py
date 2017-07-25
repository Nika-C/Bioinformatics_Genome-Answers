
A = ['A', 'GCT', 'GCC', 'GCA', 'GCG']
R = ['R', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
N = ['N', 'AAT', 'AAC']
D = ['D', 'GAT', 'GAC']
C = ['C', 'TGT', 'TGC']
Q = ['Q', 'CAA', 'CAG']
E = ['E', 'GAA', 'GAG']
G = ['G', 'GGT', 'GGC', 'GGA', 'GGG']
H = ['H', 'CAT', 'CAC']
I = ['I', 'ATT', 'ATC', 'ATA']
M = ['M', 'ATG']
L = ['L', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
K = ['K', 'AAA', 'AAG']
F = ['F', 'TTT', 'TTC']
P = ['P', 'CCT', 'CCC', 'CCA', 'CCG']
S = ['S', 'TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
T = ['T', 'ACT', 'ACC', 'ACA', 'ACG']
W = ['W', 'TGG']
Y = ['Y', 'TAT', 'TAC']
V = ['V', 'GTT', 'GTC', 'GTA', 'GTG']
Stop = ['*', 'TAA', 'TGA', 'TAG']

AA = [A, R, N, D, C, Q, E, G, H, I, M, L, K, F, P, S, T, W, Y, V, Stop]

def CodonDict():
    Dict = {}
    for i in AA:
        for j in i:
            if len(j) == 3:
                Dict[j] = i[0]
    return Dict

