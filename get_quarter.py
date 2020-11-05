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
        
        
    # Instance method
    def dayOfQuarter(self):
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

    def quarter(self):

        if(self.q2 > self.date >= self.q1):
           return 1 
            
        elif(self.q3 > self.date >= self.q2):
            return 2
            
        elif(self.q4 > self.date >= self.q3):
            return 3
            
        elif(self.date >= self.q4):
            return 4
            
        else:
            print("something went wrong")
        

for i in range(1,4):
    obj = Quarter(datetime.datetime(1994,i,i))
    print(obj.quarter())
    print(obj.dayOfQuarter())
    

# print(obj.quarter())
