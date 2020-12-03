import calendar
import datetime


date = datetime.datetime(2019,1,1)

year = date.year ; month = date.month

# creates a calendar object, sets first weekday to monday
c = calendar.Calendar(firstweekday=calendar.SUNDAY) 
# c = calendar.Calendar() 
# this returns an itterator 
monthcal = c.monthdatescalendar(year,month)

# get the third monday        
# first_sun = [day for week in monthcal for day in week if \
            # day.weekday() == calendar.MONDAY and \ 
            # day.month == month][0]

fs = []

for week in monthcal:
    for day in week:
        if day.weekday() == calendar.SUNDAY and day.month == month:
            fs.append(day)
# print(monthcal)
print(calendar.SUNDAY)
print(fs)
print(fs[0])