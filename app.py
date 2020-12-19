import csv, os, datetime 
import date_methods
import merge as m 

# when chaging, 33, 47, 43
def write_to_final(filename, method, test=False):

    if (test==True):
        ## greates a list of datetime objects for the specified range. To print them formatted us strformat
        start = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")
        end = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d")

    elif(test=="month"):
        start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
        end = datetime.datetime.strptime("2019-02-01", "%Y-%m-%d")
        filename = "month.csv"

    else:
        start = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")
        end = datetime.datetime.strptime("2100-12-31", "%Y-%m-%d")
        filename = "csvs/31-40/full_31_40.csv"

    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]



    rows = []
    # this thing itterates through all the functions in date_methods/#_#.py and writes them to a file for the specified date range
    for date in dates_generated:
        # array that we will append to array rows in line 19
        sub_rows=[]
        for name, val in method.__dict__.items():
            if callable(val):
                if (isinstance(val(date), str) or isinstance(val(date), int)):
                    sub_rows.append(val(date))



        rows.append(sub_rows)


    with open(filename, 'w') as csvfile:
    
        writer = csv.writer(csvfile)
        writer.writerow(method.feilds)
        writer.writerows(rows)

os.system("rm -r temp_csvs")
print("removing temp_csvs if it exists")
os.system("mkdir temp_csvs")
print("making temp_csvs")

write_to_final("temp_csvs/1_10.csv", date_methods.methods_1_10, True)
print("made 1_10.csv")
write_to_final("temp_csvs/11_20.csv", date_methods.methods_11_20, True)
print("makde 11_20.csv")
write_to_final("temp_csvs/21_30.csv", date_methods.methods_21_30, True)
print("made 21_30.csv")
write_to_final("temp_csvs/31_40.csv", date_methods.methods_31_40, True)
print("made 31_40.csv")
write_to_final("temp_csvs/41_50.csv", date_methods.methods_41_50, True)
print("made 41_50.csv")

print("merging csvs")
m.merge("temp_csvs/1_10.csv", "temp_csvs/11_20.csv", "temp_csvs/1_20.csv")
m.merge("temp_csvs/21_30.csv", "temp_csvs/31_40.csv", "temp_csvs/21_40.csv")
m.merge("temp_csvs/1_20.csv", "temp_csvs/21_40.csv", "temp_csvs/1_40.csv")
m.merge("temp_csvs/1_40.csv", "temp_csvs/41_50.csv", "temp_csvs/full.csv")
print("successfully merged csvs!")








