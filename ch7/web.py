
months = ["January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December"]
values = []
year = []

for i in months :
    values.append(float(input("Enter total rain for " + i + ": ")))
print()



def total():
    print("The total rainfall for the year is %.2f" % sum(values))
total()

def average():
    print("The average monthly rainfall is %.2f" % float(sum(values)/ 12))
average()

def highest():
    print("The highest monthly rainfall is", max(values))
highest()

def lowest():
    print("The lowest monthly rainfall is", min(values))
lowest()
