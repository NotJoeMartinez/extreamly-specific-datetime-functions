import datetime
import calendar
import pandas as pd

class Process:


    def __init__(self, date):
        self.date = date
        self.process_range = []
    

    def get_day_of_process(self):
        date = self.date

        # this find the thrid monday of the month of september given a date. If the previous arg has a value 
        # it gets the third mon of the previous years september
        def find_thrid_mon(date, previous=""):

            if (previous != ""):
                y = date.year - 1 
            else: 
                y = date.year 

            c = calendar.Calendar(firstweekday=calendar.MONDAY) 
            year = y ; month = 9
            monthcal = c.monthdatescalendar(year,month)
        
            third_mon = [day for week in monthcal for day in week if \
                    day.weekday() == calendar.MONDAY and \
                    day.month == month][2]

            # turn thrid_mon into a datetime object  
            dt = datetime.datetime.combine(third_mon, datetime.datetime.min.time())
            return dt 


        # if current date > third week of september of the current year 
        # return the diffrence in days between sep third of the current year and the given date
        third_mon_current = find_thrid_mon(date)

        if (date > third_mon_current):

            foo = date - third_mon_current

            return  foo.days
        else:
            foo = date - find_thrid_mon(date,"previous")
            return foo.days
             
    
    def get_month_of_process(self):
        date = self.date

        # print(date.month, date.day, self.get_day_of_process())

        while True:
            date 
            print(date)

        def find_thrid_mon(date, previous=""):

                    if (previous != ""):
                        y = date.year - 1 
                    else: 
                        y = date.year 

                    c = calendar.Calendar(firstweekday=calendar.MONDAY) 
                    year = y ; month = 9
                    monthcal = c.monthdatescalendar(year,month)
                
                    third_mon = [day for week in monthcal for day in week if \
                            day.weekday() == calendar.MONDAY and \
                            day.month == month][2]

                    # turn thrid_mon into a datetime object  
                    dt = datetime.datetime.combine(third_mon, datetime.datetime.min.time())
                    return dt








            

             

            


        
