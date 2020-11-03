#amber evans
#9/3/20
#ex 2-17
#time converter

#get a number of seconds from the user.
total_seconds= float (input('enter a number of seconds: '))

#get the number of hours
hours = total_seconds // 3600

#get the number of remaining minutes.
minutes = (total_seconds // 60) % 60

#get the number of remaining seconds.
seconds= total_seconds % 60

#display the results.
print ('here is the time in hours, minutes, and seconds:')
print ('hours: ',hours)
print ('minutes: ',minutes)
print ('seconds: ',seconds)

input()
