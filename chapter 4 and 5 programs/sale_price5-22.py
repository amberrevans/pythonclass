#Amber Evans
#9-29-2020
#program 5-22

#this program calculates a retail items
#sale price.

#DISCOUNT_PERCENTAGE is used as a global
#constant for the discount percentage.
DISCOUNT_PERCENTAGE =0.20

#The main function
def main():
    #Get the items regular price
    reg_price= get_regular_price()

    #Calculate the sale price
    sale_price=reg_price-discount(reg_price)

    #Display the sale price
    print(f'The sale price is ${sale_price:,.2f}.')

#The get_regular_price function prompts the
#user to enter an items regular price and it
#reterns that value
def get_regular_price():
    price= float(input('Enter the items regular price: '))
    return price


#The discount function accepts an items price
#as an argument and returns the amount of the
#discount, specified by DISCOUNT_PERCENTAGE.
def discount (price):
    return price*DISCOUNT_PERCENTAGE
#Call the main function
main()

