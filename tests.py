import datetime
import date_methods
import os
from get_term import Term

## greates a list of datetime objects for the specified range. To print them formatted us strformat
start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d")

# end = datetime.datetime.strptime("2019-02-01", "%Y-%m-%d")
dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# Test function below 
for date in dates_generated:
    print(Term(date).bannerTermCode())





## Stuff for testing csv
# import csv
# rows = []
# for date in dates_generated:
#     sub_rows=[]
#     sub_rows.append(date_methods.calendarWeekOfQuarter(date))
#     rows.append(sub_rows)

# filename = "19.csv"
# with open(filename, 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(rows)

    