#Amber Evans
#9-30-2020
#Exercise for gross_pay(pg229)

#This program computes gross pay
#See the heirarchy on page 229


def main():
    hrs,rate= get_input()
    gross_pay=calc_gross_pay(hrs,rate)
    print (f'Gross pay is: {gross_pay:.2f}')

def get_input():
    hours=get_hrs()
    payrate=get_rate()
    return hours, payrate

def get_hrs():
    hours=int(input('Enter hours worked:'))
    while hours <0:
        hours=int(input('Hours must be positive, re-enter hours worked: '))
    return hours

def get_rate():
    #Rate must be between 7.75 and 18.50
    payrate=float(input('Enter hourly rate: '))
    while payrate<7.75 or payrate>18.50:
        print('Rate must be between 7.75 and 18.50')
        payrate=float(input('Re-enter hourly rate: '))
    return payrate

def calc_gross_pay(hrs, rate):
    return hrs*rate

main()
