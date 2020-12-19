import datetime, math
import calendar
import numpy as np
# import methods_11_20
from objects.get_quarter import Quarter
from objects.get_term import Term
from objects.get_process import Process 

feilds = ["quarterMonth","dayOfProcess","monthOfProcess","monthNameOfProcess","monthWeekOfProcess",
"monthDayOfProcess","monthWeekDayOfProcess","isLeapYear","processYear","startDateOfProcess"]
# feilds = ["quarterMonth","dayOfProcess","monthOfProcess","monthNameOfProcess","monthWeekOfProcess",
# "monthDayOfProcess","isLeapYear","processYear","startDateOfProcess"]


def quarterMonth(date):
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    return "{}{}".format(quart,month) 

def dayOfProcess(date):
    return Process(date).get_day_of_process()

def monthOfProcess(date):
    return Process(date).get_month_of_process()

def monthNameOfProcess(date):
    return Process(date).get_month_name_of_process()

def monthWeekOfProcess(date):
    return Process(date).get_month_week_of_process() 

def monthDayOfProcess(date):
    return Process(date).get_month_day_of_process()

def monthWeekDayOfProcess(date):
    return "broken"
 
def isLeapYear(date):
    return Process(date).check_leap()

def processYear(date):
    return Process(date).get_process_year()

def startDateOfProcess(date):
    return Process(date).get_start_date_of_process()


