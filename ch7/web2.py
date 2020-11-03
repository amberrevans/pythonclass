import random
  
rainfall = open('Rainfall Data.txt', 'w')
  
for x in range(random.randint(13, 26)):
rain = str(random.randint(0,5))
rainfall.write(rain + '\n')
  
rainfall.close()

rainR = open('Rainfall Data.txt', 'r')
rainSum = 0
rainCount = 0

  
while x in rainR:
for line in range(12):
rain1 = int(line)
print(rain1)
rainSum += rain1
rainCount += 1
aveRain = rainSum / rainCount
print(format(aveRain, '.1f'))

rainfall.close()
