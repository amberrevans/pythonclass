#Amber Evans
#10-11-20
#program 6-15
#This program adds coffee to the inventory records to
#the coffee.txt file

def main():
    #Create a variable to control the loop
    another ='y'

    #Open the coffee.txt file in append mode
    coffee_file=open ('coffee.txt','a')

    #add records to the file
    while another =='y' or another =='Y':
        #get the coffee record data
        print ('Enter the following coffee data: ')
        descr= input('Description: ')
        qty= int(input('Quantity (in pounds): '))

        #append the datat to the file
        coffee_file.write(descr+ '\n')
        coffee_file.write(f'{qty}\n')

        #determine whether the user wants to add another
        #record to the file
        print ('Do you want to add another record?')
        another = input('Y= yes, anything else=no: ')

    #close the file
    coffee_file.close()
    print ('Data appended to coffee.txt')

#Call the main function
if __name__== '__main__':
    main()
    
