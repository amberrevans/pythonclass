#Amber Evans
#10-30-2020
#program 7-16
#This program saves a list of numbers to a file

def main():
    #Create a list of numbers
    numbers = [1,2,3,4,5,6,7]

    #Open a file for writing
    outfile = open('numberlist.txt','w')

    #Write the list to the file
    for item in numbers:
        outfile.write(str(item) +'\n')

    #Close the file
    outfile.close()

#Call the main function
if __name__ == '__main__':
    main()
