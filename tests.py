import datetime
import date_methods
import os
from get_term import Term
## greates a list of datetime objects for the specified range. To print them formatted us strformat
start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2100-01-01", "%Y-%m-%d")

# end = datetime.datetime.strptime("2019-02-01", "%Y-%m-%d")
dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# Test function below 
foo = Term.make_terms()
for date in dates_generated:
    print(Term.get_terms(date,foo))


    