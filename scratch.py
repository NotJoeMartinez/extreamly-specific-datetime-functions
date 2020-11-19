import methods_41_50
import datetime

date = datetime.datetime.now()

date2 = datetime.datetime(2020,8,1)

date3 = datetime.datetime(2020,9,25)

date4 = datetime.datetime(2020,9,21)
# date5.strftime("%Y-%m-%d")
def test_range():
    for i in range(1,12):
        date5 = datetime.datetime(2010,i,)
        print(methods_41_50.monthOfProcess(date5))


print(methods_41_50.monthOfProcess(date3))