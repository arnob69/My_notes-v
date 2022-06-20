# source url : https://youtu.be/-AlFiS74aQg
# source official doc : https://docs.python.org/3/library/datetime.html

from datetime import date, datetime
from time import strftime

today = date.today()

print(f"Today is : {today}")
# this will print date in the formate of yy-MM-DD
# this is a date time object

# printing the date with  specefic value
print(f"day : {today.day}")
print(f"day : {today.month}")
print(f"day : {today.year}")
# this will print month in decimal value

# to get the name of a month or day we need to use some special string formating that are availbale in the doc of datetime module
print("Printing Today's date with including the name of the day and aslo the name of the month :")

print(today.strftime("%A, %dth of %B %Y"))
# %A for week full name , %d for day of month , %B for month full name , %Y for year... to get more about this follow the offical doc

# Creating  datetime object with user specific date

Nikolas_Tesla = date(1856, 7, 10)  # yy,MM,DD
Nikolas_Tesla = date.fromisoformat("1856-07-10")
# we can also use this fromisoformat func to take input of a day in the format of YY-MM-DD
print(f"Nikola Tesla was born in : {Nikolas_Tesla}")

# working with both date and time
now = datetime.now()
print("Now we are printing not only the date but also the current time :v")
print(f"Now : {now}")
print(f"Current Time in 24hr format {now.hour}:{now.minute}:{now.second}")
now_12=now.strftime("%I:%M %p")
# To know more about this formating please checkout official doc section :v
print(f"Current Time in 12hr format {now_12}")
