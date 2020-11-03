#Amber Evans
#11-2-2020
#program exercise 7-3
#This program records monthly rain amounts and
#calculates the average, the minimun and maximum
#and total annual rainfall

#Import random number generator
import random

#Define the main function
def main():
    #Creat constants
    rows, cols = (1,1)
    
    #Define lists
    months = ['Jan','Feb','Mrc','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    rain = [[0 for rain in range (cols)] for months in range (rows)]

    #Calculate rainfall
    rain [0] = (float(random.random())*15)

    #Display results
    for cols in months:
        for rows in rain:
            print (cols,rows)
    print()

   

main()
