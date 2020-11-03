#Amber Evans
#10-7-2020
#program 6-1
#This program writes the lines of data
#to a file.

def main():
    #Open a file named philosophers.txt.
    outfile= open('philosophers.txt','w')

    #Write the names of three philosophers
    #to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    #close the file.
    outfile.close()

#Call the main function
if __name__=='__main__':
    main()
    
