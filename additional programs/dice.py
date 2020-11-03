#Amber Evans
#9-29-2020
#program 5-19

#This program the rolling of dice.
import random

#constatns for the minimum and maximum random numbers
min=1
max=6

def main():
    #Create a variable to control the loop
    again = 'y'

    #simulate rolling the dice.
    while again=='y' or again =='Y':
        print ('Rolling the dice...')
        print ('Their values are: ')
        print (random.randint(min,max))
        print (random.randint (min, max))

        #do another roll of the dice?
        again=input ('Roll them again (y=yes): ')

#call the main function.
main()

