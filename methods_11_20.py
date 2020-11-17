import datetime, math
import calendar
import numpy as np
from objects.get_quarter import Quarter
from objects.get_term import Term

feilds = ["monthNameDay","monthDayYear","monthNameDayYear","dayYear",
"yearQuarterMonthWeekDay","dayFrom1900","calendarWeekOfMonth","noncalendarWeekOfMonth",
"calendarWeekOfQuarter","noncalendarWeekOfQuarter"]

def monthNameDay(date):
    mnd = date.strftime("%B %d")
    return mnd

def monthDayYear(date):
    mdy = date.strftime("%-m/%-d/%Y")
    return mdy

def monthNameDayYear(date):
    mndy = date.strftime("%B %d, %Y")
    return mndy 

def dayYear(date):
    doy = date.strftime("%-j")
    dayYear = doy +"/"+date.strftime("%Y")
    return dayYear

def yearQuarterMonthWeekDay(date):
	# year
	year = date.strftime("%Y")
	# quarter
	quart = Quarter(date).quarter()
	# month 
	month = date.strftime("%m")
	# day of month 
	day = date.strftime("%d") 
	# week of month
	week = math.ceil(int(day)/7)

	return "{}{}{}{}{}".format(year,quart,month,week,day) 

def dayFrom1900(date):
    # date time object set at 1900
    nineteen = datetime.datetime(1900,1,1)

    # subtract nineteen from current datetime object
    daysfrom = date - nineteen

    return daysfrom.days + 2

# def get_week_of_month(date):
#     x = np.array(calendar.monthcalendar(date.year, date.month))
#     week_of_month = np.where(x==date.day)[0][0] 
#     return(week_of_month)

def calWeekOfMonth(date):
    calDayofWeek = int(date.strftime("%w")) + 1
    dom = date.strftime("%-d") 
    # calendar.setfirstweekday(6)

    # x = np.array(calendar.monthcalendar(date.year, date.month))
    # week_of_month = np.where(x==date.day)[0][0] 


    return int(((int(dom)+ 7) - calDayofWeek) / 7 )

def nonCalWeekOfMonth(date):
    day = date.strftime("%d")
    week = math.ceil(int(day)/7)
    return week
    
def calendarWeekOfQuarter(date):
    return Quarter(date).calendarWeekOfQuarter()    

def nonCalWeekOfQuarter(date):
    return Quarter(date).nonCalWeekOfQuarter()