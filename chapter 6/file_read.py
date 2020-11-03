#Amber Evans
#10-7-2020
#program 6-2
#This program reads and displays the contents
#of the phliosophers.txt file.

def main():
    #open a file named file_write.txt
    infile = open('philosophers.txt','r')

    #read the files contents
    file_contents=infile.read()

    #close the file
    infile.close()

    #print the data that was read into memory
    print(file_contents)

#call the main function.
if __name__=='__main__':
    main()
    
