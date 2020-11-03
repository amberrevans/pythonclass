#amber evans
#9/19/20
#program 4-8
#this program uses a loop to display a
#a table showing the numbers 1 through 10
#and their squares.

#print the table headings.
Print ('Number/tSquare')
print ('_______________')

#print the numbers 1 through 10
#and print their squares.

for number in range (1,11):
    square = number **2
    print (f'{number}/t{square}')
    
