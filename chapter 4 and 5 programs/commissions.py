#amber evans
#9/15/20
#program 4-1
#This program calculates sales commissions.

#create a variable to control the loop.
keep_going= 'y'

#Calculate a series of commissions.
while keep_going=='y':
    #get a salespersons sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate= float (input('Enter the commission rate: '))

    #Calculate the commisssion
    commission = sales * comm_rate

    #display the commission
    print (f'The commission is ${commission:,.2f}.')

    #see if the user wants to do another one.
    keep_going = input ('Do you want to calculate another ' +
                        'commission (Enter y for yes): ')
    
