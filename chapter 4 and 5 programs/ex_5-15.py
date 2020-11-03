#Amber Evans
#9-30-2020
#ex 5-15
#This program asks the user to enter 5 grades. It determines
#the letter grade of each, calculates the average, and
#determines that letter grade.

def main():
    test1,test2,test3,test4,test5=get_grades()
    avg=calcavg(test1+test2+test3+test4+test5)
    print('The average is: ',avg,' which is ',detgrade (avg))

def get_grades():
    tst1=int(input('Enter first test score: '))
    print('Grade is: ',detgrade(tst1))
    tst2=int(input('Enter second test score: '))
    print('Grade is: ',detgrade(tst2))
    tst3=int(input('Enter third test score: '))
    print ('Grade is: ',detgrade (tst3))
    tst4=int(input('Enter fourth test score: '))
    print ('Grade is: ',detgrade (tst4))
    tst5=int(input('Enter fifth test score: '))
    print ('Grade is: ',detgrade (tst5))
    return tst1,tst2,tst3,tst4,tst5

def detgrade(test):
    if test >=89.5:
        grade="A"
    elif test>=79.5:
        grade="B"
    elif test>=69.5:
        grade='C'
    elif test>=59.5:
        grade="D"
    else:
        grade="F"
    return grade

def calcavg(total):
    return total/5

main()
    
