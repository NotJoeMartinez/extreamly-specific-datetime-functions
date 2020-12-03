import datetime
import calendar
import pandas as pd

class Process:


    def __init__(self, date):
        self.date = date
        self.process_range = []
    
    def get_start_date_of_process(self, return_obj="", return_last=""): 
            date = self.date


            # get year
            y = date.year

            if return_last !="":
                y -= 1
            
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
            # wed = mon + datetime.timedelta(days=2)

            # check if optional arg is non null 
            if return_obj != "":
                return mon 

            # Turn wed into a full date format
            foo = mon.strftime("%Y-%m-%d %H:%M:%S.%f") 

            return foo

    def check_leap(self):
        date = self.date

        if calendar.isleap(date.year):
            return 1
        else:
            return 0
    
    def get_day_of_process(self):

        today = self.date
        last_start = self.get_start_date_of_process(True,True)
        start = self.get_start_date_of_process(True)

        if today < start:
            delta = today - last_start 
            return delta.days + 1

        elif today >= start: 
            delta = today - start
            return delta.days + 1

        else: 
            print("error starting on get_process line 91")




        # turn first into datetime object

    def get_range(self):
        """
        this finds the dates between the start date of process and 
        the first calendar week of proceading october 
        """
        date = self.date


        start = self.get_start_date_of_process(True)            

        # this looks ugly but it returns the first cal monday of october of the current year
        y = date.year; month = date.month
        year = y  
        c = calendar.Calendar(firstweekday=0) 
        monthcal = c.monthdatescalendar(year,month)
        foo = [day for week in monthcal for day in week if \
                    day.weekday() == calendar.MONDAY and \
                    day.month == month][0]

        # end date to datetime object 
        end = datetime.datetime.combine(foo, datetime.datetime.min.time())

        dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]


        return dates_generated

    def is_in_first_calweek(self):
        """
        given a date determine if it is in the first week of month STARTING SUNDAY 

        """
        date = self.date

        year = date.year ; month = date.month

        c = calendar.Calendar(firstweekday=calendar.SUNDAY) 
        # creates a 2D array of datetime objects for all week days in the month 
        monthcal = c.monthdatescalendar(year,month)

        # get all sundays of the current month and save them to first_sun 
        first_sun = []
        for week in monthcal:
            for day in week:
                if day.weekday() == calendar.SUNDAY and day.month == month:
                    first_sun.append(day)

        # turn first_sun into a datetime object  
        sun = datetime.datetime.combine(first_sun[0], datetime.datetime.min.time())

        if self.date < sun:
            return True 
        else: 
            return False

    def get_month_of_process(self):
        today = self.date
        start = self.get_start_date_of_process(True)


        delta1 = today.month + 4
        delta2 = today.month - start.month
        """
        if today is less than the start date of the process for this year,
        check if today it is in the first calendar week of the current month, 
        if today is in the first calendar week of the current month,
        return (current month number + 4) - 1.
        otherwise return current month number + 1 
        """
        if today < start:
            # if self.is_in_first_calweek() and today.month != 9:
            if self.is_in_first_calweek(): 
                return delta1 - 1 
            else:
                return delta1 

        elif today > start and today.month == 9:
            # if it's greater than start date and in september return 1
            return 1
            # if it's greater than start date but not in september return delta2
        elif today == start:
            return 1

        elif today > start: 

            if self.is_in_first_calweek():
                return delta2 
            else:
                return delta2 + 1 

    def get_month_name_of_process(self):
        """
        This is funky. This starts as "September" on the process start date 
        used with dayOfProcess. It remains as "September" until calendarWeekOfMonth 
        resets to 1, in which case it changes to "October". It will go back to 
        "September" for "month 13".
        """
        today = self.date
        start = self.get_start_date_of_process(True)

        month_map = {
            4 : "December",
            5 : "January",
            6 : "February",
            7 : "March",
            8 : "April",
            9 : "May",
            10 : "June",
            11 : "July",
            12 : "August",
            2 : "October",
            3 : "November",
            1 : "September",
            13 : "September" 
        }

        return month_map[self.get_month_of_process()]


