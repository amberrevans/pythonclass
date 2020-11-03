#Amber Evans
#10-29-2020
#program 7-7
#This program calculates the gross pay for
#each of Megans baristas

#NUM_employees is used as a constant for the
#size of the list
NUM_employees = 6

def main():
    #Create a list to hold  employee hours
    hours = [0] * NUM_employees

    #Get each employees hour worked
    for index in range (NUM_employees):
        hours [index] = float(input(f'Hours worked by employee {index+1}: '))
    #Get the hourly pay rate
    pay_rate = float(input('Hourly pay rate: '))

    #Display each employees gross pay
    for index in range (NUM_employees):
        gross_pay = hours [index] * pay_rate
        print (f'Gross pay for employee {index+1}: ${gross_pay:,.2f}')

#call the main function
if __name__=='__main__':
    main()
