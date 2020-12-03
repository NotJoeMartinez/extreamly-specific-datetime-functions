import datetime, math
import calendar
import numpy as np
# import methods_11_20
from objects.get_quarter import Quarter
from objects.get_term import Term
from objects.get_process import Process 

feilds = ["quarterMonth","dayOfProcess","monthOfProcess","monthNameOfProcess","monthWeekOfProcess",
"monthDayOfProcess","monthWeekDayOfProcess","isLeapYear","processYear","startDateOfProcess"]


def quarterMonth(date):
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    return "{}{}".format(quart,month) 

def dayOfProcess(date):
    return Process(date).get_day_of_process()

def monthOfProcess(date):
    return Process(date).get_month_of_process()

def start_date_of_process(date):
    return Process(date).get_start_date_of_process()

def monthNameOfProcess(date):
    pass

def is_leap_year(date):
    return Process(date).check_leap()