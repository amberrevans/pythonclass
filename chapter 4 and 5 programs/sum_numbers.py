#amber evans
#9-20-20
#program 4-12
#this program calculates the sum of a series of
#numbers entered by the user.

MAX= 5 # the maximum number

#initialize an accumulator variable.
total =0.0

#explain what we are doing.
print ('This program calcualtes the sum of ',end='')
print (f'{MAX} numbers you will enter.')

#get the numbers and accumulate them.
for counter in range (MAX):
    number = int(input('Enter a number: '))
    total = total + number

#display the total of the numbers.
print (f'The total is {total}.')

       
