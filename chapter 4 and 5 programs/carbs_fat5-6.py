#Amber Evans
#9-30-2020
#EX 5-6
#This program asks user to input fat grams and carbohydrate grams, then
#calculates calories from that input

def main():
    #display intro screen
    intro()
    again='y'
    #do you want to calculate another clients calories?
    while again=='y' or again=='Y':       
        #convert fat to calories
        fat_cals()
        #convert carbs to calories
        carb_cals()
    #create a variable to control the loop
        again=input('Do you want to calculate again? (y=yes): ')
    

#display intro screen
def intro():
    print('This program calculates calories from fat grams')
    print('and calories from carb grams consumed.')
    print()

#the fat_cals function calculates fat grams to calories
def fat_cals():
    fat_grams=float(input('Enter the number of fat grams consumed: '))
    while fat_grams<0:
        fat_grams=float(input('Fat grams must be positive,try again:'))
    fat_cals=fat_grams*9
    print(f'The calories from fat grams is: {fat_cals:,.2f}')

#the carb_cals function calculates carb grams to calories
def carb_cals():
    carb_grams=float(input('Enter the number of carb grams consumed: '))
    while carb_grams<0:
        carb_grams=float(input('Carb grams must be positive, try again:'))
    carb_cals=carb_grams*4
    print(f'The calories from carb grams is: {carb_cals:,.2f}')

#call the main function
main()
