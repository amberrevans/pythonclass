#Amber Evans
#9/13/20
#program 3.2
#This program calculates payroll and overtime

#Named constants to represent the base hours and
#the overtime multiplier
base_hours= 40 #base hours per week
OT_multiplier= 1.5 #overtime multiplier

#Get the hours worked and the hourly pay rate
hours= float(input('Enter the number of hours worked: '))
Pay_rate= float(input('Enter the hourly pay rate: '))

#Calculate and display the gross pay
if hours > base_hours:
    #calculate the gross pay with overtime
    #First, get the number of overtime hours worked
    overtime_hours=hours - base_hours

    #calculate the amount of overtime pay
    Overtime_pay= overtime_hours* Pay_rate* OT_multiplier

    #calculate the gross pay.
    gross_pay= base_hours* Pay_rate + Overtime_pay
else:
    
    #calcualte the gross pay without overtime
    gross_pay = hours* Pay_rate

#display the gross pay.
print (f'The gross pay is ${gross_pay:,.2f}.')
