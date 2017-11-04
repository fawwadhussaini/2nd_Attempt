def donuts(count):
    if (count < 10):
        print('Number of donuts:', count)
    else:
        print('Number of donuts: many')


donuts(9)


def both_ends(s):
    if (len(s) < 2):
        print(s)
    else:
        print (s[0:2] + s[-2:])
        print (s[0:2] + s[len(s)-2:])


both_ends ('pakistan')
