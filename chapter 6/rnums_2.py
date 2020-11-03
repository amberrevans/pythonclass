#10-13-2020
#program exercise chapter 6

#This program generates a certain amount of random numbers
#displays them, adds them, and then averages them

#import the random number generator
import random

#define the main function
def main ():

    #open a file for writing the random numbers
    random_numbers = open ('random_numbers.txt','w')

    #ask the user for number of random numbers
    qty_numbers=int(input('Enter how many random numbers should be generated: '))
    
    #validate user input
    if qty_numbers<=0:
        print ('Enter a non-negative number.')

    #create a loop to generate random numbers in the quantity specified
    for count in range (qty_numbers):
        numbers =random.randint (1,500)

        #convert the numbers to a string and write them to the file
        random_numbers.write(str(numbers)+'\n')

        #print the random numbers
        print (numbers)

    #close the file
    random_numbers.close()
    #call second function
    second('random_numbers.txt')

#calculating the sum and the average of the random numbers    
def second(file_name):
    total = 0
    rnums = 0

    #open the file for reading
    infile = open('random_numbers.txt','r')
    rnum = infile.readline()
    while rnum !='':
        
        #read the files content
        rnum = rnum.rstrip('\n')
        rnum = int(rnum)

        #add random numbers
        total+=rnum
        rnums+=1
        rnum = infile.readline()
    
    #average random numbers and close
    infile.close()
    avg = total/rnums

    #print average and sum
    print (f'The total is {total: .2f}')
    print (f'The average is {avg: .2f}')

    #Tell the user random numbers have been written to the file
    
    print ('Your randoms numbers have been written to the file')
    print ('random_numbers.txt')

main()
