#Amber Evans
#10-11-2020
#program 6-20
#This program divides a number by another number

def main():
    #get two numbers
    num1 =int(input('Enter a number: '))
    num2 =int(input('Enter another number: '))

    #divide num1 by num2 and display the results
    result = num1/ num2
    print (f'{num1} divided by {num2} is {result}')

#Call the main function
if __name__=='__main__':
    main()
    
