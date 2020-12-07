
import sys
import datetime
import os
import csv
import date_methods
import time

def test_method():
    ## greates a list of datetime objects for the specified range. To print them formatted us strformat
    start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
    end = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")

    # end = datetime.datetime.strptime("2019-02-01", "%Y-%m-%d")
    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    # remove existing csv files 
    cdir = os.getcwd()
    os.system("rm {}/csvs/tests/*.csv".format(cdir))

    # Test function below 
    # fname = datetime.datetime.now().strftime("%M_%S")
    fname = "my_try"
    file = "csvs/tests/{}.csv".format(fname)

    def makeshit(file, dates_generated): 
        for date in dates_generated:
            with open(file, 'a') as f:
                foo = date_methods.monthWeekOfProcess(date)
                # print(foo)
                # f.write(str(foo)+",{}\n".format(date.strftime("%b%d - %a")))
                f.write(str(foo)+",\n")
    

    makeshit(file,dates_generated)
    os.system("vimdiff {}/csvs/tests/test.txt {}/csvs/tests/{}.csv".format(cdir,cdir,fname))

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
    temp=pd.read_csv("csvs/sample_data.csv",usecols=methods_41_50.feilds)
    temp.to_csv('csvs/41-50/sample_41_50.csv')


# diff_check()


test_method()
