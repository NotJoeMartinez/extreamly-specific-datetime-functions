import calendar
import random
import datetime as dt
from  objects.get_process import Process 

  
def test_day_range(month):
    for day in range(1,28):
        # day = random.randint(1,14)
        # year = random.randint(2000,2019) 
        foo = dt.datetime(2018,month,day)
        print(Process(foo).get_month_of_process(), foo.strftime("%Y-%m-%d"))

# test range of months through 2018
def test_month_range():
    for month in range(1,3):
        test_day_range(month)
        # print(Process(foo).get_month_of_process(), foo.strftime("%b, %-d"))

def test_year_range():
    foo = dt.datetime(2014,1,1)
    print(Process(foo).get_start_date_of_process(), foo.strftime("%Y-%m-%d"))

