import datetime, math
import calendar
import numpy as np
from objects.get_quarter import Quarter
from objects.get_term import Term

feilds = ["bannerTermCode","termFrom1900","quarter","quarterName",
"quarterYear","quarterNameYear","yearQuarter","year","quarterMonthWeekDay","quarterMonthWeek"]

def bannerTermCode(date):
	return Term(date).bannerTermCode()

def termFrom1900(date):
	return Term(date).termFrom1900()

def quarter(date):
	return Quarter(date).quarter()

def quarterName(date):
  return "Q{}".format(Quarter(date).quarter())

def quarterYear(date):
  return "{}/{}".format(Quarter(date).quarter(),date.strftime("%Y"))

def quarterNameYear(date):
	return "Q{} {}".format(Quarter(date).quarter(),date.strftime("%Y"))

def yearQuarter(date):
	  return "{}{}".format(date.strftime("%Y"),Quarter(date).quarter())

def year(date):
      return date.strftime("%Y")

def quarterMonthWeekDay(date):
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    # day of month 
    day = date.strftime("%d") 
    # week of month
    week = math.ceil(int(day)/7)
    return "{}{}{}{}".format(quart,month,week,day) 

def quarterMonthWeek(date):
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    # day
    day = date.strftime("%d") 
    # week of month
    week = math.ceil(int(day)/7)
    return "{}{}{}".format(quart,month,week) 

# sub_rows.append(methods_31_40.bannerTermCode(date))
# sub_rows.append(methods_31_40.termFrom1900(date))
# sub_rows.append(methods_31_40.quarter(date))
# sub_rows.append(methods_31_40.quarterName(date))
# sub_rows.append(methods_31_40.quarterNameYear(date))
# sub_rows.append(methods_31_40.yearQuarter(date))
# sub_rows.append(methods_31_40.year(date))
# sub_rows.append(methods_31_40.quarterMonthWeekDay(date))
# sub_rows.append(methods_31_40.quarterMonthWeek(date))