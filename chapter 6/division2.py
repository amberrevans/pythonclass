#Amber Evans
#10-11-2020
#program 6-21
#This program divides a number by another number

def main():
    #get two number
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    #if num2 is not 0 divide num1 by num2
    #and display the results
    if num2 != 0:
        result = num1/ num2
        print (f'{num1} divided by {num2} is {result}')

    else:
        print ('Cannot divide by zero')

#call the main function
if __name__=='__main__':
    main()
    
