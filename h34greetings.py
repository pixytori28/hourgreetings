#name:Victoria Inahuazo
#email:victoria.inahuazo11@myhunter.cuny.edu
#date: 04/04/24
#this program genereates greetings by the hour

hour = int(input("Enter hour:"))

if (hour < 12):
    print("Good Morning")
elif (hour >= 12) and (hour < 17):
    print("Good Afternoon")
else:
    print("Good Evening")