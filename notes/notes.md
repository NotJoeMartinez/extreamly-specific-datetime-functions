### 2020-11-09 14:26:13

when calling the `Quarter` object in `date_methods.py` you need to pass the date argument for it to work along with the intended method. 

EX:

```python
def quarterMonthWeekDay(date):
    return Quarter(date).quarter()
```

What has me really confused is that this process is not the same for the `Term` Object.

```python
def termCode(date):
    return Term.get_terms(date,term_dict)
```

I think this is becuase in `get_quarter.py` I declared date in the constructor 

```python 
 def __init__(self, date):
        self.date = date 
```

Then in the `quarter` method I called it again like this 

```python
    def quarter(self):

        q1, q2, q3, q4 = self.q1, self.q2, self.q3, self.q4
        date = self.date
```



Meaning if I want this same behavoir in the `Term ` method I should do what I did in the `quarter` method… I think

```python
return Term(date).get_terms(term_dict)
```

This works 

### 2020-11-09 14:43:14 (39)

so we are on 39

> [quarterMonthWeekDay] 39
>  yearQuarterMonthWeekDay value without the year as the first 4 digits (204315 for April 15, 2020)

and yearQuarterMonthWeekDay is deffinded as

>  [yearQuarterMonthWeekDay] 15
>  A numerical value concatenating the year, quarter, month, noncalendarWeekOfMonth, and day (2020204315 for April 15, 2020, which is the 3rd noncalendar week of April, in the 2nd quarter)

Which I used this to make

```python
def yearQuarterMonthWeekDay(date):
    # year
    year = date.strftime("%Y")
    # quarter
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    # day of month 
    day = date.strftime("%d") 
    # week of month
    week = math.ceil(int(day)/7)

    return "{}{}{}{}{}".format(year,quart,month,week,day) 
```

This works

```python
def quarterMonthWeekDay(date):
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    # day of month 
    day = date.strftime("%d") 
    # week of month
    week = math.ceil(int(day)/7)
    return "{}{}{}{}".format(quart,month,week,day) 
```



### 2020-11-09 14:49:16 (40)

>  [quarterMonthWeek] 40 
>  quarterMonthWeekDay value without the day as the last 2 digits (2043 for April 15, 2020)

Day needs to be in this one or the week calculation will not work

```python
def quarterMonthWeek(date):
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    # day
    day = date.strftime("%d") 
    # week of month
    week = math.ceil(int(day)/7)
    return "{}{}{}".format(quart,month,week) 
```



### 2020-11-09 14:54:41 (41)

>  [quarterMonth] 41
>  quarterMonthWeek without week as the last digit (204 for April 15, 2020)

```python
def quarterMonth(date):
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    return "{}{}".format(quart,month) 
```



### 2020-11-09 14:58:47 (29)

>  [yearQuarterMonth] 29 
>  Same value as yearQuarterMonthWeekDay, albeit without the week and day as the last 3 digits (2020204 for April 15, 2020)



```python
def yearQuarterMonth(date):
    # year
    year = date.strftime("%Y")
    # quarter
    quart = Quarter(date).quarter()
    # month 
    month = date.strftime("%m")
    return "{}{}{}".format(year,quart,month)
```



### 2020-11-09 15:03:10 (33)

>  [quarter] 33
>  Quarter of the year, value is 1,2,3 or 4 depending on if the current date is on or after January 1, April 1, July 1, and October 1

```python
def quarter(date):
    return Quarter(date).quarter()
```

### 2020-11-09 15:07:29 (34)

> [quarterName] 34
>  Same numerical value as before, with a Q in front of it (Q2)

```python
def quarterName(date):
  return "Q{}".format(Quarter(date).quarter())
```

### 2020-11-09 15:10:11 (35)

>  [quarterYear] 35 
>
> Numerical value showing the quarter and year separated by a slash (2/2020)

```python
def quarterYear(date):
  return "{}/{}".format(Quarter(date).quarter(),date.strftime("%Y"))
```



### 2020-11-09 15:14:16 (36)

>  [quarterNameYear] 36 
>  The quarterName and year separated by a space (Q2 2020)

```python
def quarterName(date):
   return "Q{} {}".format(Quarter(date).quarter(),date.strftime("%Y"))
```



### 2020-11-09 15:18:38 (37)

>  [yearQuarter] 37
>  A 5 digit number with the first 4 digits being the year and the last digit being the quarter (20202 for Q2 2020)



```python
def yearQuarter(date):
	  return "{}{}".format(date.strftime("%Y"),Quarter(date).quarter())
```

### 2020-11-09 15:22:07 (38)

> [year] 38
>  The numerical value of the year (2020 for April 1, 2020)

```python
def year(date):
  return date.strftime("%Y")
```

### 2020-11-09 15:26:17 (19)

> [calendarWeekOfQuarter] 19 
>  A numerical value counting full weeks in a given quarter. If a quarter starts on a day other than Sunday, this value will be 0 until the first Sunday of a quarter, where it will start with 1. (0 for April 1, 2020)



How did I solve calendar day of week last time? 

```python
# https://stackoverflow.com/questions/3806473/python-week-number-of-the-month
def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] 
    return(week_of_month)
 
def calWeekOfMonth(date):
    calendar.setfirstweekday(6)
    
    return get_week_of_month(date.year,date.month,date.day)
```

ugh.. I coppied some stuff from stack overflow 



My problem seems to be when it asks for manual calculations



### 2020-11-09 20:20:19 (19)

calendarWeekOfQuarter

```python
  
    
    def calendarWeekOfQuarter(self):
        # determine date and quarter
        date = self.date
        quarter = self.quarter()

        # TODO: fix index out of range issue  
        # put quarters in array
        # q_array = [self.q1, self.q2, self.q3, self.q4]

        q_dict = {
            1: self.q1,
            2: self.q2,
            3: self.q3,
            4: self.q4
        }

        if (quarter == 4):
            start = q_dict[quarter]
            end = datetime.datetime(date.year+1,1,1) 
        else:
            # assign start and end dates for we can populate dates_generated[]
            start =  q_dict[quarter]
            end = q_dict[quarter + 1]


        # populate dates generated with the diffrence in days from start to end
        dates_generated = []
        for x in range(0, (end-start).days): 
            foo = start + datetime.timedelta(days=x) 
            dates_generated.append(foo)
        

        week = 0
        index = 0

        while(True):

            # adds one to the week if it is a sunday
            if (dates_generated[index].strftime("%a") == "Sun"):
                week += 1
            # if we make it to the currend day return the week number
            if (dates_generated[index] == date):
                # return "date: {} week: {}".format(date.strftime("%m/%d %a"), week)
                return week
            # breaks statment if it reaches out of index
            if (index + 1 >= len(dates_generated)):
                break

            index += 1

```

### 20 ()

> [noncalendarWeekOfQuarter] 20
>  A numerical value counting weeks in a given quarter, with the first day of the quarter having a value of 1 regardless of when the quarter starts. (1 for April 1, 2020)> 



```python
    def nonCalWeekOfQuarter(self):
        return self.calendarWeekOfQuarter() + 1

```

Added one to the return value to calendar week of quarter should do it right? 





### 26

>  [monthOfQuarter] 26
>  Numerical value counting months in a quarter. The first month of a quarter has a value of 1 (1 for April 1, 2020)

```python
    def monthOfQuarter(self):
        months_dict = {
            1: 1,
            2: 2,
            3: 3,
            4: 1,
            5: 2, 
            6: 3,
            7: 1,
            8: 2,
            9: 3, 
            10: 1,
            11: 2,
            12: 3, 
        }
        moq = months_dict[self.date.month]
        return moq 
            

```

sometimes I make things harder than they need to be. case in point while this might not be elegant it works better than the crazy logic  I wrote earlier. 



### 22

>  A numerical value counting weeks in a given year, with the first day of the year having a value of 1 regardless of when the year starts. (14 for April 1, 2020)

I'm assuming the week will start on sunday so I just added one to the calweek of year 

```python
def nonCalWeekOfYear(date):
    return int(date.strftime("%U")) + 1
```

still haven't done any diff checking 



### 31

You will need the previous definition of `termcode` to understand this one 

> [termCode] 30 
>  This is strange. Numerical value starting at 1 on January 1, 1900, incrementing up by 1 on May 11, July 1, August 21, and Jaunary 1 of the next year. So, 1/1/1900 has a value of 1, 5/11/1900 has a value of 2, 7/1/1900 has a value of 3, 8/21/1900 has a value of 4, 1/1/1901 has a value of 5, and the cycle continues. This is at least roughly aligned with our Spring (1/1-5/10), Summer I (5/10-6/30), Summer II (7/1-8/20), and Fall (8/20-12/31) terms

> [bannerTermCode] 31
>  This is also strange. Numerical value composed of the year and then either 1,2,3, or 4 to denote the term. These seem to change with the markers denoted above, and are coded suce that 2 = Spring, 3 = Summer 1, 4 = Summer II, and 1 = Fall. So, 1/1/1900 has a value of 19002, 5/11/1900 has a value of 19003, 7/1/1900 has a value of 19004, 8/21/1900 has a value of 19001, 1/1/1901 has a value of 19012

```
## Previous deff: 
spring => 1/1-5/10
summer 1 => 5/10-6/30
summer 2 => 7/1-8/20
fall => 8/20-12/31

# Modified deff
2 => spring => 1/1 through 5/10?
3 => summer1 => 5/11 through 6/30?
4 => summer2 => 7/1 through 8/20?
1= > Fall => 8/21 through 12/31?

```

No really sure if this means I need to generate a new dictionary as I did with term code or if these dates are fixed as they are in the quarters object. 

```python
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
```







### termfrom1900 (32)

>  [termFrom1900] 32
>  This is closer to common usage, but is still strange. First 4 digits are the year, last digit will always be 7. This has term identifiers like bannerTermCode, but this
>
> time we're using a convention more used by TTU. These are coded suce that 5 = Spring, 8 = Summer 1, 9 = Summer II, and 2 = Fall. So, 1/1/1900 has a value of 190057, 5/11/1900 has a value of 190087, 7/1/1900 has a value of 190097, 8/21/1900 has a value of 190027, 1/1/1901 has a value of 190157.



```
5 => spring
8 => summer 
9 => summer2
2 => fall
```

```python
    def termFrom1900(self):

        spring, summer1, summer2, fall = self.spring, self.summer1, self.summer2, self.fall

        date = self.date

        if (summer1 > date >= spring ): # spring
            return "{}{}7".format(date.strftime("%Y"),5)

        elif (summer2 > date >= summer1): # summer1
            return "{}{}7".format(date.strftime("%Y"),8)

        elif (fall > date >= summer2): # summer2
            return "{}{}7".format(date.strftime("%Y"),9) 

        elif (date >= fall): # fall
            return "{}{}7".format(date.strftime("%Y"),2)
        else: 
            print("some stupid error")
```

I'm aware that I can abstract this function but I don't think this will be as readable 