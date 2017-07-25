f = open('title.txt', 'r')

l = f.xreadlines()
for i in l:
    print 'The first line is: ', i.rstrip()
    break
