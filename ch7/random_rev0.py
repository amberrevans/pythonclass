#Amber Evans
#11-1-2020
#This program generates 20 random numbers and puts them in a list
#Then determins the total, average, highest and lowest numbers

#Import random number generator
import random

#Define the main function
def main():
    #Shows the long way source code
    print ('The long way')
    print ()

    #Generate and print list of random numbers
    numlist =[0]*20
    for index in range (20):
        numlist[index] = random.randint (1,100)
    print (numlist)
    print ()

    total =0
    min= numlist[0]
    max = numlist [0]

    for index in range (0,20):
        print (numlist [index], '', end='')
        total += numlist[index]
        if numlist [index]<min:
            min =numlist[index]
        if numlist[index]>max:
            max = numlist[index]

    print()
    print ('The total is: ',total)
    print ('The minimum value is: ',min)
    print ('The maximum value is: ',max)
    print ('The average is: ',total/20)

#Call the main function
main()
