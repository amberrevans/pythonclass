#Amber Evans
#10-8-2020
#program 6-16
#This program displays the records in the coffee.txt file

def main():
    #open the coffee.txt file
    coffee_file=open('coffee.txt','r')

    #Read the first records description field
    descr=coffee_file.readline()

    #Read the rest of the file
    while descr != '':
        #read the quantity field
        qty=float(coffee_file.readline())

        #strip the \n from the description
        descr=descr.rstrip('\n')

        #display the record
        print (f'Description: {descr}')
        print (f'Quantity: {qty}')

        #read the next description
        descr=coffee_file.readline()

    #close the file
    coffee_file.close()

#Call the main function
if __name__ =='__main__':
    main()
    
