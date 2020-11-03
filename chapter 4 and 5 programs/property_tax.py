#amber evans
#9-20-20
#program 4-13
#this program displays property taxes.

Tax_factor = 0.0065 #represents the tax factor

#get the first lot number
print ('Enter the property lot number or enter 0 to end.')
lot = int(input('Lot number: '))

#continue processing as long as the user does not enter the number 0
while lot != 0:
    #get the property value.
    value = float (input('Enter the property value: '))

    #calculate the property's tax.
    tax = value * Tax_factor

    #display the tax.
    print (f'Property tax: ${tax:,.2f}')

    #get the next lot number
    print ('Enter the next lot number or enter 0 to end.')
    lot = int (input('Lot number: '))
    
