import methods_11_20, datetime

date = datetime.datetime(2001,1,1)
foo = methods_11_20.nonCalWeekOfQuarter(date)
foo2 = methods_11_20.dayFrom1900(date)
foo3 = methods_11_20.calWeekOfMonth(date)
print(foo3 , type(foo3))