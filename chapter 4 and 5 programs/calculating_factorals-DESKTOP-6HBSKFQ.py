#amber evans
#9-21-20
#programming assignment chaper 4
#this program finds the factorial of an integer provided by the user.


#create a variable to control the loop
Keep_going= 'y'

while Keep_going =='y':

    #get input from user
    num=int(input('Enter an integer to factorial: '))

    factorial = 1

    #check if the integer is negative, positive, or zero
    #then factor

    if num<0:
        print ('Error: Please enter a non-negative integer.')
    elif num ==0:
        print ('The factorial of 0 is 1.')
    else:
        for i in range(1,num+1):
            factorial =factorial *i
    print ('The factorial of', num,'is', factorial)

    #see if user wants to factor another integer
    Keep_going= input('Do you want to calculate another '+
                      'factorial' '(enter y for yes): ')
