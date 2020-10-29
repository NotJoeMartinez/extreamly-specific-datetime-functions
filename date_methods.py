import datetime

def dateId(date):
    dateId = date.strftime("%y-%m-%d")
    return dateId

def dateType(date):
    return "date"

def fullDate(date):
    fulldate = date.strftime("%Y-%m-%d %H:%M:%S.%f") 
    return fulldate[:-3]

def day(date):
    day = date.strftime("%-d")
    return day 

def dayName(date):
    dayName = date.strftime("%A")
    return dayName

def calDayOfWeek(date):
    calDayofWeek = int(date.strftime("%w")) + 1
    return calDayofWeek

def nonCalDayOfWeek(date):
    nonCalDayOfWeek = ((int(date.strftime("%j")) - 1 ) % 7 ) + 1
    return nonCalDayOfWeek

def dayOfQuarter(date):
    # Jan
    q1 = datetime.datetime(date.year,1,1)
    # April
    q2 = datetime.datetime(date.year,4,1) 
    # July
    q3 = datetime.datetime(date.year,7,1)
    # Oct
    q4 = datetime.datetime(date.year,10,1) 


    if(q2 > date >= q1):
        # check to see if date is equal to q1
        if (date == q1):
            return 1
        # doq is day of quarter
        else:
            # subtract date by the q1 date time object
            doq = date - q1
            # get the "days" from that object
            doq = doq.days
            # turn it into an int
            int(doq)
            # add it one to it 
            return doq+1
        
    elif(q3 > date >= q2):
        if (date == q2):
            return 1
        else:
            # subtract date by the q1 date time object
            doq = date - q2
            doq = doq.days
            int(doq)
            return doq + 1

    elif(q4 > date >= q3):
        if(date == q3):
            return 1
        else: 
            # subtract date by the q1 date time object
            doq = date - q3
            doq = doq.days
            int(doq)
            return doq + 1

    elif(date >= q4):
        if(date == q4):
            return(1)
        else:
            # subtract date by the q1 date time object
            doq = date - q4
            doq = doq.days
            int(doq)
            return doq + 1

    else:
        print("something went wrong")

# A numerical value starting at 1 on January 1 and ending at 365/6 on December 31 (92 for April 1, 2020)
def dayOfYear(date):
    doy = date.strftime("%-j")
    return doy 

