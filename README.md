## This was intended to replace excel formulas for a COGNOS date dimention table 

Runing the following to produce a csv file with century of rows with 50 columns of formatted date time stamps.
```python
pip install -r requirements.txt
```

```python
python3 app.py
```
The deffinitons for each of these columns can be found in deffs.md

*** 

TODO: 
- [x] dateId 1
- [x] dateType 2 
- [x] fullDate 3
- [x] day 4
- [x] dayName 5 
- [x] calendarDayOfWeek 6
- [x] noncalendarDayOfWeek 7 
- [x] dayOfQuarter 8
- [x] dayOfYear 9
- [x] monthDay 10 
- [x] monthNameDay 11
- [x] monthDayYear 12
- [x] monthNameDayYear 13
- [x] dayYear 14
- [x] yearQuarterMonthWeekDay 15
- [x] dayFrom1900 16
- [x] calendarWeekOfMonth 17
- [x] noncalendarWeekOfMonth 18
- [x] calendarWeekOfQuarter 19
- [x] noncalendarWeekOfQuarter 20
- [x] calendarWeekOfYear 21
- [x] noncalendarWeekOfYear 22
- [x] yearQuarterMonthWeek 23
- [x] month 24
- [x] monthName 25
- [x] monthOfQuarter 26
- [x] monthYear 27
- [x] monthNameYear 28
- [x] yearQuarterMonth 29
- [x] termCode 30
- [x] bannerTermCode 31
- [x] termFrom1900 32
- [x] quarter 33
- [x] quarterName 34
- [x] quarterYear 35
- [x] quarterNameYear 36
- [x] yearQuarter 37
- [x] year 38
- [x] quarterMonthWeekDay 39
- [x] quarterMonthWeek 40
- [x] quarterMonth 41
- [x] dayOfProcess 42
- [x] monthOfProcess 43
- [x] monthNameOfProcess 44
- [x] monthWeekOfProcess 45
- [ ] monthDayOfProcess 46
- [ ] monthWeekDayOfProcess 47
- [x] isLeapYear 48
- [x] processYear 49
- [x] startDateOfProcess 50
