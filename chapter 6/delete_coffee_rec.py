#Amber Evans
#10-11-2020
#program 6-19
#This program allows the user to delete a record
#in the coffee.txt file

import os #Needed for the remove and rename functions

def main():
    #create a bool variable to use as a flag
    found = False

    #Get the coffee to delete
    search = input('Which coffee do you want to delete?')

    #open the original coffee.txt file
    coffee_file = open('coffee.txt','r')

    #open the temp file
    temp_file = open ('temp.txt','w')

    #read the first records description field
    descr = coffee_file.readline()

    #read the rest of the file
    while descr != '':
        #read the quantity field
        qty = float(coffee_file.readline())

        #strip the \n from the description
        descr=descr.rstrip('\n')

        #if this is not the record to delete then write
        #it to the temp file
        if descr != search:
            #write the record to the temp file
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty} \n')

        else:
            #set the found flag to true
            found = True
        #read the next description
        descr= coffee_file.readline()

    #close the coffee file and the temp file
    coffee_file.close()
    temp_file.close()

    #delete the original coffee.txt file 
    os.remove ('coffee.txt')

    #rename the temp file
    os.rename ('temp.txt','coffee.txt')

    #if the search value was not found in the file
    #display a message
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

#call the main function
if __name__=='__main__':
    main()
    