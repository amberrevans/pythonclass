#Amber Evans
#9-26-2020
#program 5-10
#This program demonstrates what happens when you
#change the value of a parameter.

def main():
    value =99
    print(f'The value is {value}.')
    change_me (value)
    print (f'Back in main the value is {value}.')

def change_me(arg):
    print('I am changing the value.')
    arg=0
    print(f'Now the value is {arg}.')

#call teh main function
main()

