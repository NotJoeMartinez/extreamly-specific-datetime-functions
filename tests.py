import datetime
import date_methods
import os

## greates a list of datetime objects for the specified range. To print them formatted us strformat
start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# # Test function below 
# for date in dates_generated:
#     foo = date_methods.dayYear(date)
#     print(foo)

feilds = ["dateId","dateType","fullDate","day","dayName","calendarDayOfWeek","noncalendarDayOfWeek","dayOfQuarter","dayOfYear","monthDay","monthNameDay","monthDayYear","monthNameDayYear","dayYear","yearQuarterMonthWeekDay","dayFrom1900","calendarWeekOfMonth","noncalendarWeekOfMonth","calendarWeekOfQuarter","noncalendarWeekOfQuarter","calendarWeekOfYear","noncalendarWeekOfYear","yearQuarterMonthWeek","month","monthName","monthOfQuarter","monthYear","monthNameYear","yearQuarterMonth","termCode","bannerTermCode","termFrom1900","quarter","quarterName","quarterYear","quarterNameYear","yearQuarter","year","quarterMonthWeekDay","quarterMonthWeek","quarterMonth","dayOfProcess","monthOfProcess","monthNameOfProcess","monthWeekOfProcess","monthDayOfProcess","monthWeekDayOfProcess","isLeapYear","processYear","startDateOfProcess"] 

with open("file.md", "w") as file:
    for i in feilds:
        file.write("- [ ] "+i+"\n")
    