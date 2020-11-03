#Amber Evans
#10-8-2020
#program 6-18
#this program allows the user to modify the quantity in a record
#in the coffee.txt file

import os #Needed for the remove and rename functions

def main():
    #create a bool variable to use as a flag
    found=False

    #Get the search value and the new quantity
    search=input('Enter a description to search for: ')
    new_qty=int(input("Enter the new quantity: "))

    #open the orginal coffee.txt file
    coffee_file=open ('coffee.txt','r')

    #open the temp file
    temp_file=open('temp.txt','w')

    #read the first records description field
    descr=coffee_file.readline()

    #read the rest of the file
    while descr !='':
        #read teh quantity field
        qty=float(coffee_file.readline())

        #strip the \n from the description
        descr=descr.rstrip('\n')

        #write either this record to the temp file or the new record
        #if this is the one that is to be modified
        if descr== search:
            #write the modified record to the temp file
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')
            #set the found flag to True
            found=True
        else:
            #write the original record to the temp file
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        #read the next description
        descr=coffee_file.readline()

    #close the coffee file and the temp file
    coffee_file.close()
    temp_file.close()

    #delet the original coffee.txt file
    os.remove('coffee.txt')

    #rename the temporary file
    os.rename('temp.txt','coffee.txt')

    #if the search value was not found in the file
    #display a message
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file')

#call the main function
if __name__=='__main__':
    main()
