#Amber Evans
#10-7-2020
#program 6-4
#This program gets three names from the user and writes
#them to a file

def main():
    #get three names
    print('Enter the names of three friends.')
    name1=input('friend#1: ')
    name2=input('friend#2: ')
    name3=input('friend#3: ')

    #open a file named friends.txt
    myfile=open('friends.txt.', 'w')

    #write the names to the file
    myfile.write(name1+'\n')
    myfile.write(name2+'\n')
    myfile.write(name3+'\n')

    #close the file
    myfile.close()
    print ('The names were written to friends.txt.')

#Call the main function
if __name__=='__main__':
    main()
    