#amber evans
#9/14/2020
#ex 3-9
#This program asks the user to input a pocket number on a roulette
#wheel. It then displays the color of that pocket.

pocket=int(input('Enter a pocket #: '))
if pocket ==0:
    print ('Pocket', pocket, 'is green')
elif pocket >-1 and pocket <=10:
    if pocket%2==0:
        print ('Pocket', pocket,'is black')
    else:
        print ('Pocket', pocket, 'is red')
elif pocket >=11 and pocket <=18:
    if pocket%2==0:
        print ('Pocket', pocket, 'is red')
    else:
        print ('Pocket', pocket, 'is black')
elif pocket >=19 and pocket <=28:
    if pocket%2 ==0:
        print ('Pocket' , pocket, 'is black')
    else:
        print ('Pocket', pocket, 'is red')
elif pocket >-29 and pocket <=36:
    if pocket%2 ==0:
        print ('Pocket', pocket, 'is red')
    else:
        print ('Pocket', pocket, 'is black')
else:
        print ('Invalid entry')

input ()
