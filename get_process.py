import datetime
import calendar

class Process:

    def __init__(self, date):
        self.date = date


    # TODO: calculate the calendare week of month 
    def makeRange(self):
        date = self.date
        last_day_of_month = calendar.monthrange(date.year,date.month)[1]


        start = datetime.date(date.year,date.month,1)
        end = datetime.date(date.year,date.month,last_day_of_month)

        dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]  


        return dates_generated 

    def calWeek(self):

        dates_arr = self.makeRange()
        # print(dates_arr)

        week = 0
        index = 0
        while(True):

            if(dates_arr[index].strftime("%a") == "Sun"):
                week += 1

            if (dates_arr[index].strftime("%d") == self.date.strftime("%d")):
                
                return week
                # break
            
            if(index + 1 >= len(dates_arr)):
                break
            index += 1






def test_1_12():
    for i in range(1,20):
        obj = Process(datetime.datetime(2019,1,i))
        print(obj.calWeek())

def test_calWeek():
    obj=Process(datetime.datetime(2019,1,15))
    print(obj.calWeek())



# test_calWeek()
# test_1_12()
