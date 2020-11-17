import csv, os, datetime 
import methods_1_10, methods_11_20, methods_21_30, methods_31_40


col_41_50= ["quarterMonth","dayOfProcess","monthOfProcess","monthNameOfProcess","monthWeekOfProcess",
"monthDayOfProcess","monthWeekDayOfProcess","isLeapYear","processYear","startDateOfProcess"]

def write_to_final(test=""):

    if (test=="sample"):
        ## greates a list of datetime objects for the specified range. To print them formatted us strformat
        start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
        end = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d")
        filename = ""

    elif(test=="month"):
        start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
        end = datetime.datetime.strptime("2019-02-01", "%Y-%m-%d")
        filename = "month.csv"

    else:
        start = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")
        end = datetime.datetime.strptime("2100-12-31", "%Y-%m-%d")
        filename = "csvs/31-40/full_31_40.csv"

    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]


    # rows[] is needed for line 28
    # use this to itterat through modules methods 
    # from inspect import getmembers, isfunction
    # m_1_10 = [o for o in getmembers(methods_1_10) if isfunction(o[1])]
    # m_11_20 = [o for o in getmembers(methods_11_20) if isfunction(o[1])]
    # m_21_30 = [o for o in getmembers(methods_21_30) if isfunction(o[1])]
    # m_31_40 = [o for o in getmembers(methods_31_40) if isfunction(o[1])]

    rows = []
    for date in dates_generated:
        # array that we will append to array rows in line 19
        sub_rows=[]
        for name, val in methods_31_40.__dict__.items():
            if callable(val):
                if (isinstance(val(date), str) or isinstance(val(date), int)):
                    sub_rows.append(val(date))



        rows.append(sub_rows)


    with open(filename, 'w') as csvfile:
    
        writer = csv.writer(csvfile)
        writer.writerow(methods_31_40.feilds)
        writer.writerows(rows)

write_to_final("")