def make_20(test_file):
    ## greates a list of datetime objects for the specified range. To print them formatted us strformat
    start = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")
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
                foo = date_methods.monthDayOfProcess(date)
                full_date = date.strftime("%Y-%m-%d") 
                f.write(str(foo)+"," +str(full_date)+ "\n")
                # else:
                #     f.write(str(foo)+"," +str(full_date)+ "\n")
    
    # call make_stuff()
    make_stuff(file,dates_generated)