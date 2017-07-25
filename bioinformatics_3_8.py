while True:

    s = raw_input('Searching for: ')

    if s == 'XXX':
        print 'Okay, I will stop.'
        exit()

    f = open('sequence.protein.2.fasta', 'r')
    l = f.xreadlines()
    l.readline()

    count = 0
    p = []
    for i in l:
        c = 0
        li = i.rstrip()
        for e in li:
            c += 1
            if e == s:
                p.append(count + c)

        count = count + len(li)

    print p
