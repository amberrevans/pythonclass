#amber evans
#9-20-20
#program 4-16
#this program calculates retail prices.

Mark_up = 2.5 #the markup percentage
another = 'y' #variable to control the loop

#process on or more items.
while another == 'y' or another == 'Y':
    #get the items wholesale cost
    wholesale = float (input('Enter the items wholesale cost: '))

    #validate the wholesale cost
    while wholesale <0:
        print ('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the corect ' + 'wholesale cost: '))

    #calculate the retail price
    retail= wholesale * Mark_up

    #display the retail price
    print (f'Retail price: ${retail:,.2f}')

    #do this agian?
    another = input ('Do you have another item?' + '(Enter y for yes): ')
    
    
