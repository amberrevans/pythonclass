#Amber Evans
#10-8-2020
#program 6-9
#This program reads all of the values in the sales.txt file

def main():
    #open the sales.txt file for reading
    sales_file=('sales.txt','r')

    #read the first line from the file, but
    #dont convert to a number yet. we still
    #need to test for an empty string
    line=sales_file.readline()

    #as long as an empty string is not returned from
    #readline, continue processing
    while line !='':
        #convert line to a float
        amount=float (line)

        #format and display the amount
        print(f'{amount:.2f}')

        #read teh next line
        line=sales_file.readline()

    #close the file
    sales_file.close()

#call the main function
if __name__ =='__main__':
    main()
    
