import datetime
import csv
# Term Code
# This is strange. Numerical value starting at 1 on January 1, 1900, incrementing up by 1 on May 11, July 1, 
# August 21, and Jaunary 1 of the next year. So, 1/1/1900 has a value of 1, 5/11/1900 has a value of 2, 7/1/1900 
# has a value of 3, 8/21/1900 has a value of 4, 1/1/1901 has a value of 5, and the cycle continues. This is at least roughly 
# aligned with our Spring (1/1-5/10), Summer I (5/10-6/30), Summer II (7/1-8/20), and Fall (8/20-12/31) terms


# this thing creates a list in the range of datetime objects starting from 1900 to whatever date you supplied it 
# it then checks eacho of those date time objects to see if they match up with one of the 4 term dates

def make_terms():

    # starting at jan 1 1900 make a list of datetime objects up until date 
    start = datetime.datetime(1900,1,1)
    end = datetime.datetime(2100,1,1)
    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    # list of "term enders"
    term_strs = ["01-01","05-11","07-01","08-21"]

    # Iteration counter 
    i = 0
    # Term counter
    term = 0

    # TermDates dictionary 

    term_dict = {}
    # not sure if this is needed 
    while(True):

        #  the d_index formating is neccisary to check against out term_strs which triggers the counter
        d_index = dates_generated[i].strftime("%m-%d") 

        if any(d_index in s for s in term_strs):
            term +=1
            # print(term,dates_generated[i].strftime("%Y-%m-%d"))
            term_dict[dates_generated[i].strftime("%Y-%m-%d")] = term 

        if(i+1 >= len(dates_generated)):
            break
        i+=1

    return term_dict


        
def get_terms(date):
    term_dict = make_terms()

    q1 = datetime.datetime(date.year,1,1)
    q2 = datetime.datetime(date.year,5,11)
    q3 = datetime.datetime(date.year,7,1)
    q4 = datetime.datetime(date.year,8,21)

    step = datetime.datetime(date.year + 1, 1,1)

    if ( q2 > date >= q1):
        print("is between 1 - 5: Jan - May")
    elif( q3 > date >= q2 ):
        print("is between 5/11 - 7/0")
    elif(q4 > date >= q3):
        print("is between 7/1 and 8, 21")
    elif(step > date > q4):
        print("is between 8/21 and 01/01 of the proceading year")


    # print(str_month)


    
    # print(term_dict)
    # print(term,type(term))




get_terms(datetime.datetime(2005,9,1))

# get_terms(datetime.datetime(dates_generated[i].strftime("%Y-%m-%d") ,1,1))
# get_terms()