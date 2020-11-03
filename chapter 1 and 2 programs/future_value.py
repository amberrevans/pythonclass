#amber Evans
#9/6/20
#program 2-18
#this program calculates future value

#Get the desired future value
future_value=float(input('enter the desired future value: '))

#get the annual interest rate
rate= float(input('enter the annual interest rate: '))

#get the number of years that the money will appreciate
years=int(input('enter the number of years the money will grow: '))

#calculate the amount needed to deposit
present_value=future_value/ (1.0 +rate) **years

#display the amount needed to deposit
print ('you will need to deposit this amount: ', present_value)
