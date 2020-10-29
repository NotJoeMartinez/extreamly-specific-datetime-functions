import csv, os, datetime 
import date_methods

filename = "tabels.csv"

# feilds = ["dateId","dateType","fullDate","day","dayName","calendarDayOfWeek","noncalendarDayOfWeek","dayOfQuarter","dayOfYear","monthDay","monthNameDay","monthDayYear","monthNameDayYear","dayYear","yearQuarterMonthWeekDay","dayFrom1900","calendarWeekOfMonth","noncalendarWeekOfMonth","calendarWeekOfQuarter","noncalendarWeekOfQuarter","calendarWeekOfYear","noncalendarWeekOfYear","yearQuarterMonthWeek","month","monthName","monthOfQuarter","monthYear","monthNameYear","yearQuarterMonth","termCode","bannerTermCode","termFrom1900","quarter","quarterName","quarterYear","quarterNameYear","yearQuarter","year","quarterMonthWeekDay","quarterMonthWeek","quarterMonth","dayOfProcess","monthOfProcess","monthNameOfProcess","monthWeekOfProcess","monthDayOfProcess","monthWeekDayOfProcess","isLeapYear","processYear","startDateOfProcess"]
feilds = ["dateId","dateType", "fullDate", "day", "dayName" ]


## greates a list of datetime objects for the specified range. To print them formatted us strformat
start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]


# rows[] is needed for line 28
rows = []

for date in dates_generated:
    # array that we will append to array rows in line 19
    sub_rows=[]

    dateId = date_methods.dateId(date)
    sub_rows.append(dateId)

    dateType = date_methods.dateType(date)
    sub_rows.append(dateType)

    fullDate = date_methods.fullDate(date)
    sub_rows.append(fullDate)

    day = date_methods.

    #append to rows in row 19    
    rows.append(sub_rows)



with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(feilds)
    writer.writerows(rows)



