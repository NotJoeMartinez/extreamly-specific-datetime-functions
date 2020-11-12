import datetime, math
import calendar
import numpy as np
from objects.get_quarter import Quarter
from objects.get_term import Term

feilds_11_20 = ["monthNameDay","monthDayYear","monthNameDayYear","dayYear",
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
    dayYear = dayOfYear(date)+"/"+date.strftime("%Y")
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

    return daysfrom.days

def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] 
    return(week_of_month)

def calWeekOfMonth(date):
    calendar.setfirstweekday(6)
    
    return get_week_of_month(date.year,date.month,date.day)

def nonCalWeekOfMonth(date):
    day = date.strftime("%d")
    week = math.ceil(int(day)/7)
    return week
    
def calendarWeekOfQuarter(date):
    return Quarter(date).calendarWeekOfQuarter()    

def nonCalWeekOfQuarter(date):
    return Quarter(date).nonCalWeekOfQuarter()