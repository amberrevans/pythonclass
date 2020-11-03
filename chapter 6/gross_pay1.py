#Amber Evans
#10-11-2020
#program 6-22
#This program calculates gross pay

def main():
    #get the number of hours worked
    hours = int(input('How many hours did you work? '))

    #Get the hourly pay rate
    pay_rate = float(input('Enter your hourly pay rate: '))

    #Calculate the gross pay
    gross_pay = hours* pay_rate

    #display the gross pay
    print (f'Gross pay: ${gross_pay:,.2f}')

#Call the main function
if __name__=='__main__':
    main()