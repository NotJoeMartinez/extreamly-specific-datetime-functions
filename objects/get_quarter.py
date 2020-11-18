# https://realpython.com/python3-object-oriented-programming/
import datetime
import math
class Quarter:

    def __init__(self, date):
        self.date = date 
        # Jan
        self.q1 = datetime.datetime(date.year,1,1)
        # April
        self.q2 = datetime.datetime(date.year,4,1) 
        # July
        self.q3 = datetime.datetime(date.year,7,1)
        # Oct
        self.q4 = datetime.datetime(date.year,10,1) 
    
    # Makes a range of date time dynamic to the date time object passed to it
    def makeRange(self):
        date = self.date
        quarter = self.quarter()

        q_dict = {
            1: self.q1,
            2: self.q2,
            3: self.q3,
            4: self.q4
        }

        if (quarter == 4):
            start = q_dict[quarter]
            end = datetime.datetime(date.year+1,1,1) 
        else:
            # assign start and end dates for we can populate dates_generated[]
            start =  q_dict[quarter]
            end = q_dict[quarter + 1]

        dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        return dates_generated

    def dayOfQuarter(self):

        q1, q2, q3, q4 = self.q1, self.q2, self.q3, self.q4
        date = self.date

        if(q2 > date >= q1):
            # check to see if date is equal to q1
            if (date == q1):
                return 1
            # doq is day of quarter
            else:
                # subtract date by the q1 date time object
                doq = date - q1
                # get the "days" from that object
                doq = doq.days
                # turn it into an int
                int(doq)
                # add it one to it 
                return doq+1

        elif(q3 > date >= q2):
            if (date == q2):
                return 1
            else:
                # subtract date by the q1 date time object
                doq = date - q2
                doq = doq.days
                int(doq)
                return doq + 1

        elif(q4 > date >= q3):
            if(date == q3):
                return 1
            else: 
                # subtract date by the q1 date time object
                doq = date - q3
                doq = doq.days
                int(doq)
                return doq + 1

        elif(date >= q4):
            if(date == q4):
                return(1)
            else:
                # subtract date by the q1 date time object
                doq = date - q4
                doq = doq.days
                int(doq)
                return doq + 1

        else:
            print("something went wrong")

    # prints out the quarter
    def quarter(self):


        q1, q2, q3, q4 = self.q1, self.q2, self.q3, self.q4
        date = self.date
        
        if(q2 > date >= q1):
           return 1 
            
        elif(q3 > date >= q2):
            return 2
            
        elif(q4 > date >= q3):
            return 3
            
        elif(date >= q4):
            return 4
            
        else:
            print("something went wrong")

    # Numerical value counting months in a quarter. 
    def monthOfQuarter(self):

        month = self.date.month
        q = self.quarter()

        if (q == 1):

            return month 

        elif(q == 2):

            return month - 3
        
        elif(q == 3):
            return month - 6 
        
        else:
            return month - 9
    
    def calendarWeekOfQuarter(self):
        date = self.date
        # I = Day of quarter
        doc = self.dayOfQuarter()
        # G = Cal Day of week
        calDayofWeek = int(date.strftime("%w")) + 1
        # =INT(((7+I)-G)/7)
        final = ((7 + doc) - calDayofWeek)/7
        return int(final)
        # determine date and quarter
        quarter = self.quarter()

        q_dict = {
            1: self.q1,
            2: self.q2,
            3: self.q3,
            4: self.q4
        }

        if (quarter == 4):
            start = q_dict[quarter]
            end = datetime.datetime(date.year+1,1,1) 
        else:
            # assign start and end dates for we can populate dates_generated[]
            start =  q_dict[quarter]
            end = q_dict[quarter + 1]

        dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        

        week = 0
        index = 0

        while(True):

            # adds one to the week if it is a sunday
            if (dates_generated[index].strftime("%a") == "Sun"):
                week += 1
            # if we make it to the currend day return the week number
            if (dates_generated[index] == date):
                # return "date: {} week: {}".format(date.strftime("%m/%d %a"), week)
                return week
            # breaks statment if it reaches out of index
            if (index + 1 >= len(dates_generated)):
                break

            index += 1
    
        
    def nonCalWeekOfQuarter(self):
        i = self.dayOfQuarter()

        return int( ((i-1)/7) + 1 )


    def monthOfQuarter(self):
        months_dict = {
            1: 1,
            2: 2,
            3: 3,
            4: 1,
            5: 2, 
            6: 3,
            7: 1,
            8: 2,
            9: 3, 
            10: 1,
            11: 2,
            12: 3, 
        }
        moq = months_dict[self.date.month]
        return moq 
            








# for i in range(1,13):
# obj = Quarter(datetime.datetime(2019,1,1))

# print(obj.monthOfQuarter())



#     print("The quarter is {}".format(obj.quarter()))
#     print("The month of the quarter is {}".format(obj.monthOfQuarter()))
#     print("The day of the quarter is {}".format(obj.dayOfQuarter()))
    
