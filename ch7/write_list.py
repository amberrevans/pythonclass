#Amber Evans
#10-30-2020
#program 7-14
#This program saves a list of strings to a file

def main():
    #Create a list of stirngs
    cities = ['New York', 'Boston','Atlanta', 'Dallas']

    #open a file for writing
    outfile =open('cities.txt', 'w')

    #Write the list to the file
    for item in cities:
        outfile.write (item + '\n')

    #Close the file
    outfile.close()

#Call the main function
if __name__ =='__main__':
    main()
        
