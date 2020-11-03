#Amber Evans
#10-8-2020
#program 6-10
#This program uses the for loop to read
#all of the values in the sales.txt file

def main():
    #open the sales.txt file for reading
    sales_file=open('sales.txt','r')

    #Read all the lines from the file
    for line in sales_file:
        #convert line to a float
        amount=float (line)
        #format and display amount
        print(f'{amount:.2f}')

    #close the file
    sales_file.close()

#call the main function
if __name__=='__main__':
    main()
    
