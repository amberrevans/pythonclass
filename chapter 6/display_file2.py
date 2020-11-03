#Amber Evans
#10-11-2020
#program 6-25
#This program displays the contents of a file

def main():
    #Get the name of a file
    filename = input('Enter a filename: ')

    try:
        #open the file
        infile = open(filename, 'r')

        #read the files contents
        contents = infile.read()

        #Display the files contents
        print (contents)

        #close the file
        infile.close()

    except IOError:
        print('An error occured trying to read')
        print('the file', filename)

#call the main function
if __name__=='__main__':
    main()
    
