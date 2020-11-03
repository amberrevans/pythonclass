#Amber Evans
#10-12-2020
#random numbers file

#This program is for ch 6 exercises

#import the random number generator
import random

#calculates the sum and average of the random numbers
def comp_sum_avg(file_name):
    total =0
    rnums = 0
    #Open the file for reading
    try:
        infile=open(file_name,'r')
    except IOError:
        print ('File does not exist')
    else:
        rnum=infile.readline()
        
        while rnum!='':
            try:
                rnum= int(rnum)
                
            except:
                print (rnum)
                total +=rnum
                rnums+=1
                rnum=infile.readline()

        #print (linenum+':'+rnum)
        infile.close()
        avg= total/rnums
        print (f'The total is {total:.2f}')
        print (f'The average is {avg:.2f}')
        
#define the main function
def main():

    #open a file for writing the random numbers
    random_numbers = open ('random_numbers.txt','w')

    #get the number of random numbers to be generated
    qty_numbers=int(input('Enter how many random numbers should be generated: '))

    #display the random list of numbers
    print ('Your list of random numbers: ')

    #create a loop to generate the random numbers in the quantity specified
    for count in range (qty_numbers):
        number = random.randint (1,500)

        #convert the numbers to a string an write the to the file
        random_numbers.write(str(number)+'\n')

    #close the file
    random_numbers.close()

    #Tell user numbers have been written to the file
    comp_sum_avg('random_numbers.txt')
    print ('Your random numbers have been written to the file')
    print('random_numbers.txt')

#call the main function
main()
