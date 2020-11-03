#Amber Evans
#10-8-2020
#program 6-13
#This program gets employee data from the user and saves
#it as records in the employee.txt file

def main():
    #Get the number of employee records to create
    num_emps=int(input('How many employee records '+
                       'do you want to create?'))

    #open a file for writing
    emp_file=open('employees.txt','w')

    #Get each employees data and write it to the file
    for count in range(1, num_emps+1):
        #get the data for an employee
        print (f'Enter data for employee #{count}')
        name=input('Name: ')
        id_num=input('ID number: ')
        dept=input ('Department: ')

        #write the data as a record to the file
        emp_file.write(f'{name}\n')
        emp_file.write(f'{id_num}\n')
        emp_file.write(f'{dept}\n')

        #Display a blank line
        print()

    #close the file
    emp_file.close()
    print('Employee records written to employees.txt.')

#call the main function
if __name__=='__main__':
    main()
    
