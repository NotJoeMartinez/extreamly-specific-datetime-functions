import datetime, math
from get_quarter import GetQuarter
from get_term import Term
import calendar
import numpy as np

# Date in the format of yearMonthDay (example 20200401 is April 1, 2020)
def dateId(date):
    dateId = date.strftime("%Y%m%d")
    return dateId

# This column is 'Date' for all rows
def dateType(date):
    return "date"

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

# This is a numerical value that starts at 1 for January 1 of a given year and increments up to 7 before going back to 1. 
# The value is 1 for January 1, 2020, even though the date was a Wednesday (which should have a value of 4). A week here 
# seems to be defined as groups of 7 days starting with 1/1. (1 for for April 1, 2020) 
def nonCalDayOfWeek(date):
    nonCalDayOfWeek = ((int(date.strftime("%j")) - 1 ) % 7 ) + 1
    return nonCalDayOfWeek

# A numerical value starting at 1 on January 1, April 1, July 1, and October 1, incrementing up until the first day of the next quarter is reached. 
def dayOfQuarter(date):
    doc = GetQuarter(date)
    return(doc.dayOfQuarter())

# A numerical value starting at 1 on January 1 and ending at 365/6 on December 31 (92 for April 1, 2020)
def dayOfYear(date):
    doy = date.strftime("%-j")
    return doy 

# A yearless date in the format of month/day (4/1 for April 1) 
def monthDay(date):
    md = date.strftime("%-m/%-d")
    return md

# A yearless date in the format of monthName day (April 01) 
def monthNameDay(date):
    mnd = date.strftime("%B %d")
    return mnd

# monthDayYear A date in the format of m/d/yyyy (4/1/2020) 
def monthDayYear(date):
    mdy = date.strftime("%-m/%-d/%Y")
    return mdy

# monthNameDayYear A date in the format of monthName day, year (April 01, 2020) 
def monthNameDayYear(date):
    mndy = date.strftime("%B %d, %Y")
    return mndy 

# dayYear A field combining dayOfYear and the current year, separated by a / (92/2020 for April 1, 2020) 
def dayYear(date):
    dayYear = dayOfYear(date)+"/"+date.strftime("%Y")
    return dayYear


# yearQuarterMonthWeekDay A numerical value concatenating the 
# year, quarter, month, noncalendarWeekOfMonth, and day (2020204315 for April 15, 2020, 
# which is the 3rd noncalendar week of April, in the 2nd quarter) 
def yearQuarterMonthWeekDay(date):
    # year
    year = date.strftime("%Y")
    # quarter
    quart = GetQuarter(date)
    quart = quart.quarter()
    # month 
    month = date.strftime("%m")
    # day of month 
    day = date.strftime("%d") 
    # week of month
    week = math.ceil(int(day)/7)

    return "{}{}{}{}{}".format(year,quart,month,week,day) 

# dayFrom1900
# A numerical value counting days up from 1/1/1900 (43922 for April 1, 2020)
# for some reason this is offset by three days from by sample data
def dayFrom1900(date):
    # date time object set at 1900
    nineteen = datetime.datetime(1900,1,1)

    # subtract nineteen from current datetime object
    daysfrom = date - nineteen

    return daysfrom.days

# calendarWeekOfMonth
# A numerical value counting full weeks in a given month. If a month starts on a day other than Sunday, this value will be 0 until 
# the first Sunday of a month, where it will start with 1. (0 for April 1, 2020)

# https://stackoverflow.com/questions/3806473/python-week-number-of-the-month
def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] 
    return(week_of_month)

def calWeekOfMonth(date):
    calendar.setfirstweekday(6)
    
    return get_week_of_month(date.year,date.month,date.day)


# nonCalendarWeekOfMOnth
# A numerical value counting weeks in a given month, with the first day of the month having a value of 1 regardless of when the month starts. (1 for April 1, 2020) 
def nonCalWeekOfMonth(date):
    day = date.strftime("%d")
    week = math.ceil(int(day)/7)
    return week


# nonCalWeekOfQuarter 20
# A numerical value counting full weeks in a given quarter. If a quarter starts on a day other than Sunday, 
# this value will be 0 until the first Sunday of a quarter, where it will start with 1. (0 for April 1, 2020) 
def calWeekOfQuarter(date):
    pass

# 21
def calendarWeekOfQuarter(date):
    pass 


# A numerical value counting full weeks in a given year. If a year starts on a day 
# other than Sunday, this value will be 0 until the first Sunday of a year, where it will start with 1. (13 for April 1, 2020) 
def calendarWeekOfYear(date):
    return date.strftime("%-U")

def yearQuarterMonthWeek(date):
    pass

# 24 
def month(date):
    return date.strftime("%-m")

# 25
def monthName(date):
    return date.strftime("%B")

# 26
def monthOfQuarter(date):
    pass

# 27 
def monthYear(date):
   return date.strftime("%-m/%Y")

# 28
# Date in the format of monthName, year (April, 2020 for April 1, 2020) 
def monthNameYear(date):
    return date.strftime("%B, %Y")

# 29
def yearQuarterMonth(date):
    pass

# TermCode

term_dict = Term.make_terms()
def termCode(date):
    return Term.get_terms(date,term_dict)





