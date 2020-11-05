# https://realpython.com/python3-object-oriented-programming/
import datetime
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
        
        
    def dayOfQuarter(self):

        # q1, q2, q3, q4 = self.q1, self.q2, self.q3, self.q4

        # date = self.date
        if(self.q2 > self.date >= self.q1):
            # check to see if date is equal to q1
            if (self.date == self.q1):
                return 1
            # doq is day of quarter
            else:
                # subtract date by the q1 date time object
                doq = self.date - self.q1
                # get the "days" from that object
                doq = doq.days
                # turn it into an int
                int(doq)
                # add it one to it 
                return doq+1

        elif(self.q3 > self.date >= self.q2):
            if (self.date == self.q2):
                return 1
            else:
                # subtract date by the q1 date time object
                doq = self.date - q2
                doq = doq.days
                int(doq)
                return doq + 1

        elif(self.q4 > self.date >= self.q3):
            if(self.date == self.q3):
                return 1
            else: 
                # subtract date by the q1 date time object
                doq = self.date - q3
                doq = doq.days
                int(doq)
                return doq + 1

        elif(self.date >= q4):
            if(self.date == q4):
                return(1)
            else:
                # subtract date by the q1 date time object
                doq = self.date - q4
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
        






for i in range(1,13):
    obj = Quarter(datetime.datetime(1994,i,i))

    print(obj.quarter())
    

