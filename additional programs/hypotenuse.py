#Amber Evans
#9-30-2020
#program 5-26
#This program calculates the legth of a right
#triangles hypotenuse

import math

def main():
    #Get the length of the triangles two sides
    a=float(input('Enter the length of side A: '))
    b=float(input('Enter the length of side B: '))

    #Calculate the length of the hypotenuse
    c=math.hypot(a,b)

    #Display the length of the hypotenuse
    print(f'The length of the hypotenuse is {c}.')

#call the main function
main()
