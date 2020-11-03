#amber evans
#9/9/2020
#this program gets three test scores and displays
#their average. It congratulates the user if the
#average is a high score.

#the High_score named constant holds the value that is
#considered a high score.
High_score= 95

#get the three test scores
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

#calculate the average test score.
average = (test1+test2+test3) / 3

#print the average.
print (f'The average score is {average}.')

#if the average is a high score
#congratulate the user.
if average >= High_score:
    print('Congratulations!')
    print ('that is a great average!')
    
