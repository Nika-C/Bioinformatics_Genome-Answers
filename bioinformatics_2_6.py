Str = raw_input('Enter a string: ')

L = list(Str)
L.reverse()
rStr = ''
for i in L:
    rStr = rStr + i

print 'Reversed string: ' + rStr
