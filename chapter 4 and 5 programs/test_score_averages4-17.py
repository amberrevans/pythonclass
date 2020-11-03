#amber evans
#9-21-20
#program 4-17
#this program averages test scores. It asks the user for the
#number of students and the number of test scores per student.

#get the number of students
num_students = int(input('How many students do you have?'))

#get the number of test scores per student.
num_test_scores= int(input('How many test scores per student?'))

#determine each students average test score
for student in range (num_students):
    #initialize an accumulator for the test scores
    total = 0.0

    #display the student number.
    print (f'Student number {student + 1}')
    print ('___________________')

    #get the students test scores
    for test_num in range (num_test_scores):
        print (f'Test number {test_num+1}', end='')
        score = float (input(':'))

        #add the score to the accumulator
        total+= score

    #calculate the average test score for this student.
    average = total/ num_test_scores

    #display the average.
    print (f'The average for student number {student +1}'
           f' is: {average:.1f}')
    print ()
    
