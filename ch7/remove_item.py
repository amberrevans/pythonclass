#Amber Evans
#10-29-2020
#program 7-6
#This program demonstrates how to use the remove
#method to remove an item from the list

def main():
    #Create a list with some items
    food = ['Pizza','Burgers','Chips']

    #Display the list
    print('Here are the items in the food list: ')
    print (food)

    #Get the item to change
    item = input('Which item should I remove? ')

    try:
        #Remove the item
        food.remove(item)

        #Display the list
        print ('Here is the revised list: ')
        print (food)

    except ValueError:
        print('That item was not found in the list.')

#Call the main function
if __name__=='__main__':
    main()
