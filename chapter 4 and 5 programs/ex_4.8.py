#amber evans
#9/23/2020
#ex 4-8
#this program sums numbers input by the user

total=0
num=int(input('Enter a positive number, negative to end: '))
while num>=0:
    total+=num
    num=int(input('Enter another positive number, negative to end: '))
print ('The total is:', total)
