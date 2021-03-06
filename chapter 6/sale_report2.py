#Amber Evans
#10-11-2020
#program 6-27
#This program displays the total of the amounts
#in the sales_data.txt file

def main():
    #initialize an accumulator
    total = 0.0

    try:
        #open the sales_data.txt file
        infile = open('sales_data.txt','r')

        #read the values from the file
        #and accumulate them
        for line in infile:
            amount = float (line)
            total += amount
        #close the file
        infile.close()

        #print the total
        print (f'{total:,.2f}')
    except:
        print ('An error occurred.')

#Call the main function
if __name__=='__main__':
    main()
