#Amber Evans
#10/22/2020
#program 7-4
#This program demonstrates how to get the index
#of an item in a list and then replace
#that item with a new item

def main():
    #Create a list with some items.
    food = ['Pizza', 'Burgers','Chips']

    #display the list
    print ('Here are the items in the food list: ')
    print (food)

    #Get the item to change
    item = input('Which item should I change? ')

    try:
        #get the items index tin the list
        item_index = food. index(item)

        #get the value to replace it with
        new_item = input('Enter the new value: ')

        #Replace the old item with the new item
        food[item_index] = new_item

        #display the list
        print('Here is the revised list: ')
        print (food)
    except ValueError:
        print('That item was not found in the list.')
#Call the main function
if __name__== '__main__':
    main()
    
