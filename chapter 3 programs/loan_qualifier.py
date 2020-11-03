#amber evans
#9/13/2020
#program 3.5
#this program as a loan qualifier

min_salary = 30000.0 #minimum annual salary
min_years = 2       #minimun years on the job

#Get the customer's annual salary
salary = float (input('Enter your annual salary: '))

#Get the number of years on the current job
years_on_job = int(input('Enter the number of '+
                         'years employed: '))
#Determine whether the customer qualifies
if salary >= min_salary:
    if years_on_job >= min_years:
        print ('You qualify for the loan.')
    else:
        print (f'You must have been employed '
               f' for at least {min_years} '
               f' years to qualify.')
else:
    print (f'You must earn at least $'
           f'{min_salary:,.2f} '
           f' per year to qualify.')
    
