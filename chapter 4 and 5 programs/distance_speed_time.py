#amber evans
#9/23/2020
#ex 4-4
#This program determines distance traveld, based on input
#speed and time.

speed= int(input('Enter the speed of the vehicle in MPH: '))
hours= int(input('Enter the number of hours traveled: '))
print ()
print ('Hours   Distance Traveled')
print('--------------------------')
for hour in range (1, hours+1):
    dist=hour*speed
    print (hour,'\t\t',dist)
    
