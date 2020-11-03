#Amber Evans
#9-30-2020
#ex 5-16

#This program generates a random number, determins if it's odd or even,
#then computes the total number of odd and even numbers.

import random

def main():
    numodd=0
    numeven=0
    for index in range(1,101):
        num=random.randint(1,1000)
        if num % 2==0:
            numeven+=1
        else:
            numodd+=1
        print (num)

    print (numeven, numodd)

main()
