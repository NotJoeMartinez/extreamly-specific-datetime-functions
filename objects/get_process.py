import datetime
from datetime import timedelta
import calendar
import pandas as pd
import logging


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
        """
        if today is less than the start date of the process for this year,
        check if today it is in the first calendar week of the current month, 
        if today is in the first calendar week of the current month,
        return (current month number + 4) - 1.
        otherwise return current month number + 1 
        """
        today = self.date
        start = self.get_start_date_of_process(True)


        delta1 = today.month + 4
        delta2 = today.month - start.month

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

    def get_month_week_of_process(self):
        """
        This is funky. A (integer?) starting with the monthOfProcess  value as the first 1-2 digits 
        and ending with a modified calendarWeekOfMonth as the last 2 digits. Take for 
        example the week that connects October 2019 - November 2019. The last 5 days of 
        October have "calendarWeekOfMonth" of 4, while the first 2 days of November have a 
        "calendarWeekOfMonth" of 0 (as "calendarWeekOfMonth isn't set to 1 until the first Sunday of a month). 
        This "monthWeekOfProcess" column will use "4" for those 5 days in October and will use "5" for 
        those first 2 days in November.
        """
        
        today = self.date.date()
        year = today.year
        month = today.month 

        c = calendar.Calendar(firstweekday=calendar.SUNDAY) 
        # creates a 2D array of datetime objects for all week days in the month 
        monthcal = c.monthdatescalendar(year,month)
        
        week_of_month = "error"
        
        #  logging.basicConfig(filename='debug.log', filemode='w', level=logging.DEBUG)
        # determine if the month starts on a sunday
        first_day_of_month = today - timedelta(days = int(today.strftime("%d"))-1)

        #  last_day_of_prev_month = first_day_of_month - timedelta(days=1)

        #  if first_day_of_month == :

        if monthcal[0][0].month == today.month:
            start_index = 1 
        else:
            start_index = 0
        # week of month
        for counter, week in enumerate(monthcal, start=start_index):

            if today in week and counter == 0 and today.month != 3:
                week_of_month = 5 
            # if I am in march and march starts on a monday return 5 else return 4
            elif today in week and counter == 0 and today.month == 3: 
                # check to see if the first day of month is a sunday 
                if first_day_of_month.strftime("%a") == "Mon":
                    week_of_month = 4
                else:
                    week_of_month = 5
                    

            elif today in week:
                week_of_month = counter



        # month of process
        month_of_process = self.get_month_of_process()
        
        # find the index of the current date within this 2D array
        return "{}0{}".format(month_of_process,week_of_month)

    def get_process_year(self):
        """
         This is a 4 digit year representing the year of the fall term for which we are signing up students. 
         Whenever we cross over past a new "start of process date" (3rd Wednesday in September), this will 
         increment by 1. For 9-16-2019, the "processYear" value is 2020, as on this date we are starting to 
         sign people up for Fall 2020 housing. Once the date cycles around to the next "start of process date" 
         on 9/21/2020, the year increments to 2021 (as we would have normally started signing up for Fall 2021 
         starting on/around that date).
        """
        today = self.date
        start_date_of_process = self.get_start_date_of_process(return_obj="True")
        
        # if current date is greater than or equal to the start date of process of current year
        # return the current year plus one, otherwise return the current year 
        if today >= start_date_of_process:
            return today.year + 1
        else:
            return today.year
    
    def get_month_day_of_process(self):
        """
         This is also funky. This is starts with the monthOfProcess value and ends with a value counting 
         days within that month. In general, this counts days up from 1 whenever "monthOfProcess" resets to 1. 
         However, this does not cleanly count up from 1 once we get to the end of the month and the start of a 
         new month. It seems a formula for this column is based on the week calculated by "monthWeekOfProcess". 
         Using our example before of October 2019 - November 2019: 10/31/2019 has an expected value of 226 
         (2nd "month of process", 26th day since the month started). The following day 11/1/2019 has a value of 234. 
         I'm guessing the formula for this saw this was a Friday of Week 5 and said the day value must then be 34 
         (4 full weeks + 6 days = 34).
        """
