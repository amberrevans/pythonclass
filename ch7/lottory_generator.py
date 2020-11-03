#Amber Evans
#11-1-2020
#program exercise 7-2

#This program generates a 7 digit lottery number


#Import random number generator
import random

#Define the main function
def main():
    
    lotnum = [0]*7
    for index in range (7):
        lotnum[index] = random.randint (0,9)
    print (lotnum)

    for index in range (7):
        print (lotnum[index], end='')

#Call the main function
main ()
