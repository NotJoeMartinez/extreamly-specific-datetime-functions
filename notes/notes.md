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

 [quarterName] 34
 Same numerical value as before, with a Q in front of it (Q2)

```python
def quarterName(date):
  return "Q{}".format(Quarter(date).quarter())
```

### 2020-11-09 15:10:11 (35)

 [quarterYear] 35 

 Numerical value showing the quarter and year separated by a slash (2/2020)

```python
def quarterYear(date):
  return "{}/{}".format(Quarter(date).quarter(),date.strftime("%Y"))
```


