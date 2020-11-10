import datetime
import csv
# TODO: turn this into an object 

# Term Code
# This is strange. Numerical value starting at 1 on January 1, 1900, incrementing up by 1 on May 11, July 1, 
# August 21, and Jaunary 1 of the next year. So, 1/1/1900 has a value of 1, 5/11/1900 has a value of 2, 7/1/1900 
# has a value of 3, 8/21/1900 has a value of 4, 1/1/1901 has a value of 5, and the cycle continues. This is at least roughly 
# aligned with our Spring (1/1-5/10), Summer I (5/10-6/30), Summer II (7/1-8/20), and Fall (8/20-12/31) terms

class Term:

    def __init__(self,date):
        self.date = date

        # terms         
        self.spring = datetime.datetime(date.year,1,1)
        
        self.summer1 = datetime.datetime(date.year,5,11) 

        self.summer2 = datetime.datetime(date.year,7,1)

        self.fall = datetime.datetime(date.year,8,21) 

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


        
    def get_terms(self,term_dict):

        date = self.date

        q1 = datetime.datetime(date.year,1,1)
        q2 = datetime.datetime(date.year,5,11)
        q3 = datetime.datetime(date.year,7,1)
        q4 = datetime.datetime(date.year,8,21)

        step = datetime.datetime(date.year + 1, 1,1)
        # print(step)

        if ( q2 > date >= q1):
            return term_dict[q1.strftime("%Y-%m-%d")]

        elif( q3 > date >= q2 ):
            return term_dict[q2.strftime("%Y-%m-%d")]
            
        elif(q4 > date >= q3):
            return term_dict[q3.strftime("%Y-%m-%d")]

        elif(step > date >=q4):
            return term_dict[q4.strftime("%Y-%m-%d")]
        # if step is accasble in the dict return a value 
        elif(step.strftime("%Y-%m-%d") in term_dict):
            return term_dict[step.strftime("%Y-%m-%d")]
        else:
            return
    
    def bannerTermCode(self):

        spring, summer1, summer2, fall = self.spring, self.summer1, self.summer2, self.fall

        date = self.date

        if (summer1 > date >= spring ):
            return "{}{}".format(date.strftime("%Y"),2)
        elif (summer2 > date >= summer1):
            return "{}{}".format(date.strftime("%Y"),3)
        elif (fall > date >= summer2):
            return "{}{}".format(date.strftime("%Y"),4)
        elif (date >= fall):
            return "{}{}".format(date.strftime("%Y"),1)
        else: 
            print("some stupid eror")


# obj = Term(datetime.datetime(2019,1,1))
# print(obj.termCode())