import datetime, math
import calendar
import numpy as np
from objects.get_quarter import Quarter
from objects.get_term import Term

feilds = ["calendarWeekOfYear","noncalendarWeekOfYear",
"yearQuarterMonthWeek","month","monthName","monthOfQuarter","monthYear","monthNameYear",
"yearQuarterMonth","termCode"]


def calendarWeekOfYear(date):
    return date.strftime("%-U")

def nonCalWeekOfYear(date):
    doy = date.strftime("%j")
    ncwoy = ((int(doy) - 1)/7) + 1
    return int(ncwoy)

def yearQuarterMonthWeek(date):
    year = date.strftime("%Y")
    # quarter
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    # this will not work without day
    day = date.strftime("%d") 
    # week 
    week = math.ceil(int(day)/7)
    return "{}{}{}{}".format(year,quart,month,week)

def month(date):
    return date.strftime("%-m")

def monthName(date):
    return date.strftime("%B")

def monthOfQuarter(date):
    return Quarter(date).monthOfQuarter()

def monthYear(date):
   return date.strftime("%-m/%Y")

# Date in the format of monthName, year (April, 2020 for April 1, 2020) 
def monthNameYear(date):
    return date.strftime("%B, %Y")

def yearQuarterMonth(date):
    year = date.strftime("%Y")
    # quarter
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    # day of month 
    return "{}{}{}".format(year,quart,month)

# TermCode
term_dict = Term.make_terms()
def termCode(date):
    return Term(date).get_terms(term_dict)


