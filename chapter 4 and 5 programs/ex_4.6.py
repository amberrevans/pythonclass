#amber evans
#9/23/2020
#ex 4-6
#this program produces a table of celcius values from 0 to 20
#and the corresponding fahrenheit value

print ()
print ('Celcius   Fahrenheit')
print('---------------------')
for tempc in range (0,21):
    tempf=tempc*1.8+32
    print (tempc, '\t  ',f' {tempf: .2f}')
