import datetime
import calendar
import numpy as np
class Process:


    def __init__(self, date):
        self.date = date
        self.process_range = []
    

    # this produces an array of datetime objects for the month of the  
    # it should return a dictionary with each day mapped to a number and datetime object
    def make_process_dict(self):
        date = self.date

        def get_week_of_month(year, month, day):
            x = np.array(calendar.monthcalendar(year, month))
            week_of_month = np.where(x==day)[0][0] 
            return(week_of_month)

        calendar.setfirstweekday(6)
        week_om = get_week_of_month(date.year,date.month,date.day)


        week = 0
        index = 0

        while(True):
            
            if(dates_arr[index].strftime("%a") == "Sun"):
                week += 1
            
            if(dates_arr[index].strftime("%a") == "Mon" and week == 3):
                
                return dates_arr[index]



            if (index + 1 >= len(dates_arr)):
                break
            else:
                index += 1
        
def make_process_dict():
    obj = Process(datetime.datetime(2019,1,1)).make_process_dict()
    print(obj)


make_process_dict()