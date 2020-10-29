# https://realpython.com/python3-object-oriented-programming/
import datetime
class GetQuarter:


    def __init__(self, date):
        self.date = date 
    
    # Instance method
    def dayOfQuarter(self):
        # Jan
        q1 = datetime.datetime(self.date.year,1,1)
        # April
        q2 = datetime.datetime(self.date.year,4,1) 
        # July
        q3 = datetime.datetime(self.date.year,7,1)
        # Oct
        q4 = datetime.datetime(self.date.year,10,1) 

        # TODO: find a way to return the quarter    
        # determin is quarter is not null if so return the quarter

        if(q2 > self.date >= q1):
            # check to see if date is equal to q1
            if (self.date == q1):
                return 1
            # doq is day of quarter
            else:
                # subtract date by the q1 date time object
                doq = self.date - q1
                # get the "days" from that object
                doq = doq.days
                # turn it into an int
                int(doq)
                # add it one to it 
                return doq+1
            
        elif(q3 > self.date >= q2):
            if (self.date == q2):
                return 1
            else:
                # subtract date by the q1 date time object
                doq = self.date - q2
                doq = doq.days
                int(doq)
                return doq + 1

        elif(q4 > self.date >= q3):
            if(self.date == q3):
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
