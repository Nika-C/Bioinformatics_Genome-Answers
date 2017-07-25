while True:

    p = raw_input('Position: ')

    if p == 'XXX':
        print 'Okay, I will stop.'
        exit()
    else:
        try:
            p = int(p)
        except:
            continue
    f = open('sequence.protein.2.fasta', 'r')
    l = f.xreadlines()

    l.readline()
    count = 0
    for i in l:
        li = i.rstrip()
        count = count + len(li)

        if count > p:
            pli = p - count + len(li)
            print li [ pli-1 : pli+2 ]
            break

