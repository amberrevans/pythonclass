#amber evans
#9/19/20
#program 4-9
#This program converts the speeds 60kph
#through 130kph (in 10kph increments)
#to mph.

Start_speed= 60     #starting speed
End_speed= 131      #ending speed
Increment= 10       #speed increment
Conversion_factor= 0.6214   #conversion factor

#print the table headings.
print ('KPH\tMPH')
print('----------')

#print the speeds.
for kph in range (Start_speed, End_speed, Increment):
    mph=kph*Conversion_factor
    print (f'{kph}\t {mph:.1f}')
    
