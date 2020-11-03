import datetime
# Term Code
# This is strange. Numerical value starting at 1 on January 1, 1900, incrementing up by 1 on May 11, July 1, 
# August 21, and Jaunary 1 of the next year. So, 1/1/1900 has a value of 1, 5/11/1900 has a value of 2, 7/1/1900 
# has a value of 3, 8/21/1900 has a value of 4, 1/1/1901 has a value of 5, and the cycle continues. This is at least roughly 
# aligned with our Spring (1/1-5/10), Summer I (5/10-6/30), Summer II (7/1-8/20), and Fall (8/20-12/31) terms

# class Term():

#     termDict = {
#         1 : "Jan, 1",
#         2 : "May, 11",
#         3 : "July, 1"
#     }


#     def __init__ (self, date):
#         self.date = date
#         self.first = ""


def which_term(date):
    # starting at jan 1 1900 make a counter that moves up every 
    count = 0

    start = datetime.datetime(1900,1,1)
    end = date

    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    term_strs = ["01-01","05-11","07-01","08-21"]
    i = 0
    term = 0
    # if any("abc" in s for s in some_list):
    # while(datetime.datetime(1901,1,1) > dates_generated[i]):
    while(date>dates_generated[i]):
        d_index = dates_generated[i].strftime("%m-%d") 
        # print(d_index)
        if any(d_index in s for s in term_strs):
            term +=1
            print(term,d_index)
        # print(i)
        if(i+1 >= len(dates_generated)):
            break
        i+=1


        
    
    pass
    # return "{}, {}".format(len(dates_generated),type(dates_generated[23]))

        


    
print(which_term(datetime.datetime(1901,1,1)))
