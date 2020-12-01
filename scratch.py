import calendar
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



for i in dates:
    print(Process(i).get_day_of_process())



