import datetime
# import date_methods
import os
import csv
import app
import methods_11_20, methods_21_30, methods_31_40
# from get_term import Term
# from objects.get_process import Process

def test_method():
    ## greates a list of datetime objects for the specified range. To print them formatted us strformat
    start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
    end = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d")

    # end = datetime.datetime.strptime("2019-02-01", "%Y-%m-%d")
    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    # Test function below 

    for date in dates_generated:
        print(Process(date).get_day_of_process())

def test_csv():
    # Stuff for testing csv
    import csv
    rows = []
    for date in dates_generated:
        sub_rows=[]
        sub_rows.append(Process(date).calWeek())
        rows.append(sub_rows)

    filename = "test.csv"
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


# check for diffrences between csv files
import pandas as pd
def diff_check():
    temp=pd.read_csv("csvs/accurate_sample_data.csv",usecols=methods_31_40.feilds)
    # temp_test =  pd.read_csv("1-10.csv", usecols=app.feilds1)
    temp.to_csv('sample_31_40.csv')


diff_check()


