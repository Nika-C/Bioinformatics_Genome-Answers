
Dict = {}

while True:
    c = raw_input('Enter three-base codon to build: ')

    if c == 'XXX':
        print 'Okay, I will switch'
        break
    else:
        a = raw_input('Enter amino-acid: ')
        Dict[c] = a

while True:
    c_q = raw_input('Enter three-base codon to search: ')
    
    if c_q == 'XXX':
        print 'Okay, I will stop.'
        break
    else:
        print 'Amino acid for ' + c_q + ': ' + Dict[c_q]

