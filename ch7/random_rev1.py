#Amber Evans
#11-1-2020
#program exercise 7-4

#This porgram generates 20 random number and puts them in a list.
#Then determines the total, average, highest and lowest numbers.

#import random number generator
import random

#Define main function
def main():
    #Prints the short way information
    print ('The short way')
    print ()

    #Generate the random numbers and create a list
    numlist = [0]*20
    for index in range (20):
        numlist [index] = random.randint(1,100)
    print (numlist)
    print ()

    #Create accumulator
    total = 0
    for rnum in numlist:
        print(rnum, "",end ='')
        total+=rnum
    print()

    #Print total, average, highest, and lowest numbers for user
    print('The total is: ',total)
    print ('The minimum value is: ',min(numlist))
    print ('The maximum value is: ',max(numlist))
    print ('The average is: ',total/20)

#Call the main function
main()
