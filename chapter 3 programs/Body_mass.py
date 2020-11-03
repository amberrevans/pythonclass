#Amber Evans
#9/14/2020
#program 3-14
#This program calculated body mass, then tells user if they are optimal, under
#or over weight.

#This is a body mass calculator.
Weight= int(input('Enter your body weight in pounds: '))
Height= int(input('Enter your height in inches: '))

#calculate the Body Mass index for the user.
BMI= Weight*(703/(Height*Height))

#print the users BMI
print(f'Your body mass index is {BMI:.2f}.')

#defines optimal, under, and over weight
if BMI>= 18.5 and BMI<=25:
    print ('Your body mass index is optimal.')
if BMI < 18.5:
    print ('You are under weight.')
if BMI> 25:
    print ('You are over weight.')
input()
