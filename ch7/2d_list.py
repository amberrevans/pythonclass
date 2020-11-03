#Amber Evans
#11-1-2020
#program 2D list
#This program populates a 2D list with random numbers. Then totals the rows
#totals the columns, and left and right diagonals

#Import random number generator
import random

#Define the main function
def main():
    #Create the 2D list
    ROWS, COLS = (3,3)
    vals = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    #Populate the list with random numbers and print it
    for row in range (ROWS):
        for col in range (COLS):
            vals[row][col] = random.randint (1,9)
    print (vals)
    print()

    for row in range (ROWS):
        for col in range (COLS):
            print (vals[row][col], '',end = '')
        print()

    #Calculate the row totals
    for row in range (ROWS):
        rtotal =0
        for col in range (COLS):
            rtotal+=vals[row][col]
        print ('Row', row+1,'total is',rtotal)
    print()

    #Calculate the column totals
    for col in range (COLS):
        ctotal = 0
        for row in range (ROWS):
            ctotal+=vals[row][col]
        print ('Column',col+1,'total is',ctotal)
    print()

    #Calculate the diagonals
    ldiag = vals[0][0]+ vals [1][1] + vals [2][2]
    rdiag = vals[0][2] + vals [1][1] + vals [2][0]
    print ('Left diagonal is', ldiag)
    print ('Right diagonal is', rdiag)

#Call the main function
main()
