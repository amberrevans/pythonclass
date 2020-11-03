#Amber Evans
#10-8-2020
#program 6-14

#This program displays the records that are in
#the employee.txt file

def main():
    #Open the employee.txt file
    emp_file=open('employees.txt','r')

    #Read the first line from the file, which is
    #the name field of the first record
    name=emp_file.readline()

    #if a field was read, continue processing
    while name!='':
        #read the ID number field
        id_num=emp_file.readline()

        #read the department field
        dept=emp_file.readline()

        #Strip the newlines from the fields
        name=name.rstrip('\n')
        id_num=id_num.rstrip('\n')
        dept= dept.rstrip('\n')

        #Display the record
        print(f'Name: {name}')
        print(f'ID: {id_num}')
        print(f'Dept: {dept}')

        #read the name field of the next record
        name=emp_file.readline()

    #close the file
    emp_file.close()

#call the main function
if __name__=='__main__':
    main()
    
