#amber evans
#9/15/20
#program 4-2
#This program assists a technician in the process
#of checking a substances temperature.

#named constant to represent the maximum temperature
Max_temp = 102.5

#get the substances temperature
temperature= float(input('Enter the substances Celsius temperature: '))

#as long as necessary, instruct the user to
#adjust the thermostat

while temperature > Max_temp:
    print('The temperature is too high.')
    print('Turn the thermostate down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature= float(input('Enter the new Celsius temperature: '))

#remind the user to check the temperature again
#in 15 minutes
print ('The temperature is acceptable.')
print ('Check it again in 15 minutes.')
          
