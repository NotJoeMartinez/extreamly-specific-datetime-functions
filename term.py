import datetime
import csv
# Term Code
# This is strange. Numerical value starting at 1 on January 1, 1900, incrementing up by 1 on May 11, July 1, 
# August 21, and Jaunary 1 of the next year. So, 1/1/1900 has a value of 1, 5/11/1900 has a value of 2, 7/1/1900 
# has a value of 3, 8/21/1900 has a value of 4, 1/1/1901 has a value of 5, and the cycle continues. This is at least roughly 
# aligned with our Spring (1/1-5/10), Summer I (5/10-6/30), Summer II (7/1-8/20), and Fall (8/20-12/31) terms


# this thing creates a list in the range of datetime objects starting from 1900 to whatever date you supplied it 
# it then checks eacho of those date time objects to see if they match up with one of the 4 term dates

def which_term(date):

    # starting at jan 1 1900 make a list of datetime objects up until date 
    start = datetime.datetime(1900,1,1)
    end = date
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
    while(date>dates_generated[i]):

        #  the d_index formating is neccisary to check against out term_strs which triggers the counter
        d_index = dates_generated[i].strftime("%m-%d") 

        if any(d_index in s for s in term_strs):
            term +=1
            # print(term,dates_generated[i].strftime("%Y-%m-%d"))
            term_dict[term] = dates_generated[i].strftime("%Y-%m-%d") 

        if(i+1 >= len(dates_generated)):
            break
        i+=1

    return term_dict

        
    

        

# TODO: Somehow turn the string back into a datetime object and determin what term the given term number is based on the datetime object
    
yee = which_term(datetime.datetime(2100,1,10))

f = open("dict.txt", "w")
f.write(str(yee))
f.close

