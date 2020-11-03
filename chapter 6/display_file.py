#Amber Evans
#10-11-2020
#program 6-24
#This program displays the contents of a file

def main():
    #Get the name of a file
    filename = input('Enter a filename: ')

    #Opent the file
    infile = open(filename,'r')

    #Read the files contents
    contents = infile.read()

    #Display the files contents
    print (contents)

    #Close the file
    infile.close()

#Call the main function
if __name__== '__main__':
    main()
    
