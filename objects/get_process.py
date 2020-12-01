import datetime
import calendar
import pandas as pd

class Process:


    def __init__(self, date):
        self.date = date
        self.process_range = []
    

    
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


    def get_start_date_of_process(self): 
            date = self.date

            # get year
            y = date.year
            
            year = y ; month = 9

            # creates a calendar object, sets first weekday to monday
            c = calendar.Calendar(firstweekday=0) 

            # this returns an itterator 
            monthcal = c.monthdatescalendar(year,month)

            # get the third monday        
            third_mon = [day for week in monthcal for day in week if \
                    day.weekday() == calendar.MONDAY and \
                    day.month == month][2]

            # turn thrid_mon into a datetime object  
            mon = datetime.datetime.combine(third_mon, datetime.datetime.min.time())

            # get wednesday by adding two 
            wed = mon + datetime.timedelta(days=2)

            # Turn wed into a full date format
            foo = wed.strftime("%Y-%m-%d %H:%M:%S.%f") 

            return foo

            
    def check_leap(self):
        date = self.date

        if calendar.isleap(date.year):
            return 1
        else:
            return 0
    

    def get_day_of_process(self):
        print(self.get_start_date_of_process())







            

             

            


        
