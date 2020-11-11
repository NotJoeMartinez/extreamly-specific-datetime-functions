import datetime
import calendar

class Process:

    def __init__(self, date):
        self.date = date


    # TODO: calculate the calendare week of month for third 
    def makeRange(self):
        date = self.date
        last_day_of_month = calendar.monthrange(date.year,9)[1]


        start = datetime.date(date.year,9,1)
        end = datetime.date(date.year,9,last_day_of_month)

        dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]  

        dates_generated.append(self.date)

        return dates_generated 

    def threeCalWeek(self):

        dates_arr = self.makeRange()
        # print(dates_arr, self.date)
        # print(dates_arr)

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
    
        






def test_1_12():
    for i in range(1,20):
        obj = Process(datetime.datetime(2019,1,i))
        print(obj.calWeek())

def test_threeCalWeek():
    foo = []
    for i in range (2010, 2019):
        obj=Process(datetime.datetime(i,1,15))
        foo.append(obj.threeCalWeek())
        print(foo)
        if (len(foo)>=2):
            foo.pop(0)



test_threeCalWeek()
# test_1_12()
