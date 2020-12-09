import calendar
import random
import datetime as dt
from  objects.get_process import Process 

dates = [
        dt.datetime(2010,5,5),
        dt.datetime(2011,5,5),
        dt.datetime(2012,5,5),
        dt.datetime(2013,5,5),
        dt.datetime(2014,5,5),
        dt.datetime(2015,5,5)
]

  
  
def test_day_range():
    for day in range(1,28):
        # day = random.randint(1,14)
        # year = random.randint(2000,2019) 
        foo = dt.datetime(2019,10,day)
        print(Process(foo).get_month_of_process(), foo.strftime("%b, %-d, %a"))

# test range of months through 2018
def test_month_range():
    for month in range(1,12):
        day = random.randint(1,28)
        foo = dt.datetime(2018,month,day)
        print(Process(foo).get_process_year(), foo.strftime("%b, %-d"))


test_month_range()