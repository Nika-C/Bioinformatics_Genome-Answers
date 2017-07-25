num = input('Which times table: ')

if num not in range(1, 10):
    print 'What?'
    exit()

for i in range(1,10):
    print '%d * %d = %d' % (num, i, num * i)

