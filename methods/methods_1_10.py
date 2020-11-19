import datetime, math
import calendar
import numpy as np
from objects.get_quarter import Quarter
from objects.get_term import Term

feilds = ["dateId","dateType","fullDate","day","dayName","calendarDayOfWeek","noncalendarDayOfWeek",
"dayOfQuarter","dayOfYear","monthDay"]
# Date in the format of yearMonthDay (example 20200401 is April 1, 2020)
def dateId(date):
    dateId = date.strftime("%Y%m%d")
    return dateId

# This column is 'Date' for all rows
def dateType(date):
    return "Date"

# Standard SQL datetime value in the format of year-month-day 00:00:00.000 (2020-04-01 00:00:00.000)
def fullDate(date):
    fulldate = date.strftime("%Y-%m-%d %H:%M:%S.%f") 
    return fulldate[:-3]

# Numerical value of the day of the month (1 for April 1, 2020)
def day(date):
    day = date.strftime("%-d")
    return day 

#  Name of day of the week (Wednesday for April 1, 2020)
def dayName(date):
    dayName = date.strftime("%A")
    return dayName

# Numerical representation for day of the week (4 for Wednesday, April 1, 2020)
def calDayOfWeek(date):
    calDayofWeek = int(date.strftime("%w")) + 1
    return calDayofWeek

def nonCalDayOfWeek(date):
    nonCalDayOfWeek = ((int(date.strftime("%j")) - 1 ) % 7 ) + 1
    return nonCalDayOfWeek

# A numerical value starting at 1 on January 1, April 1, July 1, and October 1, incrementing up until the first day of the next quarter is reached. 
def dayOfQuarter(date):
    doc = Quarter(date)
    return(doc.dayOfQuarter())

# A numerical value starting at 1 on January 1 and ending at 365/6 on December 31 (92 for April 1, 2020)
def dayOfYear(date):
    doy = date.strftime("%-j")
    return doy 

# A yearless date in the format of month/day (4/1 for April 1) 
def monthDay(date):
    md = date.strftime("%-m/%-d")
    return md


