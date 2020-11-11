import datetime
import calendar

class Process:


    def __init__(self, date):
        self.date = date
        self.process_range = []
    

    # this produces an array of datetime objects for the month of the  
    # it should return a dictionary with each day mapped to a number and datetime object
    def make_process_dict(self):
        date = self.date

        last_day_of_september = calendar.monthrange(date.year,9)[1]

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
        
        def getDayOfProcess(self, start, end):

            date = self.date

            dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]  

            index = 1

            while(True):
                if (date == dates_generated[index]):
                    return index, date

                index+=1


            return


        





def test_threeCalWeek():
    foo = []
    for i in range (2019,2021):
        obj=Process(datetime.datetime(i,1,15))
        foo.append(obj.threeCalWeek())

        if (len(foo) > 1):
            print(foo)
        if (len(foo)>=2):
            foo.pop(0)


# test_threeCalWeek()

# this works in the test.py file
# for date in dates_generated:

#     foo = []
#     for i in range(start.year, end.year+1):
#         obj=Process(datetime.datetime(i,date.month,date.day))
#         foo.append(obj.threeCalWeek())
#         if (len(foo) > 1):
#             print(foo)
#         if (len(foo)>=2):
#             foo.pop(0)

