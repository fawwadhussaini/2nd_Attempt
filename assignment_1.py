def donuts(count):
    if (count < 10):
        print('Number of donuts:', count)
    else:
        print('Number of donuts: many')

donuts(9)

def both_ends(s):
    if (len(s) < 2):
        print('')
    else:
        #print (s[0:2] + s[-2:8])
        print (s[0:2] + s[len(s)-2:])

both_ends ('pakistan')

def fix_start (f):
    print (f[0:1] + f[1:].replace('c','^'))

fix_start ('cricket by chance')

def mix_up (a,b):
    e = a + ' ' + b
    print (e)
    d = a[0:2] + b[2:]
    c = b[0:2] + a[2:]
    e = c + ' ' + d
    print (e)

mix_up('pepsi','cola')

def verbing(v):
    if (len(v)>=3):
        if(v[-3:len(v)] == 'ing'):
            print ( v + 'ly')
        else:
            print ( v + 'ing')
    else:
        print (v)

