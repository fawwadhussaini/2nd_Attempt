def Odd_number(x):
    for a in range(1,x):
        if (a%2!=0):
            print (a, ' is an odd number')

Odd_number(30)

# Program to check either a number is prime or not!
def Prime_number(i):
        for a in range(2,i):
            if(i % a) == 0:
                break
        else:
                print('Yes', i, 'is a prime number')


Prime_number (19)


def Prime_numbers(x):
    for i in range(2,x+1):
        for a in range(2,i):
            if(i % a) == 0:
                break
        else:
                print(i, 'is a prime number')

Prime_numbers (19)