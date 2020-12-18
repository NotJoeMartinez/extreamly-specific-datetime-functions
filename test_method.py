
import sys
import datetime
import os
import csv
import date_methods
import time

def test_method(test_file):
    ## greates a list of datetime objects for the specified range. To print them formatted us strformat
    start = datetime.datetime.strptime("1900-01-01", "%Y-%m-%d")
    end = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d")

    # end = datetime.datetime.strptime("2019-02-01", "%Y-%m-%d")
    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    # remove existing csv files 
    cdir = os.getcwd()
    os.system("rm /home/supernova/Desktop/tests/my_try.csv")

    # Test function below 
    fname = "my_try"
    file = "/home/supernova/Desktop/tests/{}.csv".format(fname)

    def make_stuff(file, dates_generated): 
        for date in dates_generated:
            with open(file, 'a') as f:
                foo = date_methods.monthOfProcess(date)
                full_date = date.strftime("%Y-%m-%d") 
                f.write(str(foo)+"," +str(full_date)+ "\n")
                # else:
                #     f.write(str(foo)+"," +str(full_date)+ "\n")
                # print(foo)
                # f.write(str(foo)+",{}\n".format(date.strftime("%b%d - %a")))
                # if date.strftime("%A") == "Sunday":
                #     f.write(str(foo)+"," +str(full_date)+ ","+str(date.strftime("%A")) + "\n")
                # else:
                
    
    # call make_stuff()
    make_stuff(file,dates_generated)
    # run vimdiff against new csv generate
    # os.system("vimdiff {}/csvs/tests/{} {}/csvs/tests/{}.csv".format(cdir,test_file,cdir,fname))

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


test_method("test_45.txt")
