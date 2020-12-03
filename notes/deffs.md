[dateId] 1
 Date in the format of yearMonthDay (example 20200401 is April 1, 2020)

 [dateType] 2 
 This column is 'Date' for all rows

 [fullDate] 3 
 Standard SQL datetime value in the format of year-month-day 00:00:00.000 (2020-04-01 00:00:00.000)

 [day] 4
 Numerical value of the day of the month (1 for April 1, 2020)

 [dayName] 5 
 Name of day of the week (Wednesday for April 1, 2020)

 [calendarDayOfWeek] 6 
 Numerical representation for day of the week (4 for Wednesday, April 1, 2020)

 [noncalendarDayOfWeek] 7
 This is a numerical value that starts at 1 for January 1 of a given year and increments up to 7 before going back to 1. The value is 1 for January 1, 2020, even though the date was a Wednesday (which should have a value of 4). A week here seems to be defined as groups of 7 days starting with 1/1. (1 for for April 1, 2020)

 [dayOfQuarter] 8
 A numerical value starting at 1 on January 1, April 1, July 1, and October 1, incrementing up until the first day of the next quarter is reached.

 [dayOfYear] 9
 A numerical value starting at 1 on January 1 and ending at 365/6 on December 31 (92 for April 1, 2020)

 [monthDay] 10 
 A yearless date in the format of month/day (4/1 for April 1)

 [monthNameDay] 11
 A yearless date in the format of monthName day (April 01)

 [monthDayYear] 12 
 A date in the format of m/d/yyyy (4/1/2020)

 [monthNameDayYear] 13
 A date in the format of monthName day, year (April 01, 2020)

 [dayYear] 14
 A field combining dayOfYear and the current year, separated by a / (92/2020 for April 1, 2020)

 [yearQuarterMonthWeekDay] 15
 A numerical value concatenating the year, quarter, month, noncalendarWeekOfMonth, and day (2020204315 for April 15, 2020, which is the 3rd noncalendar week of April, in the 2nd quarter)

 [dayFrom1900] 16
 A numerical value counting days up from 1/1/1900 (43922 for April 1, 2020)

 [calendarWeekOfMonth] 17
 A numerical value counting full weeks in a given month. If a month starts on a day other than Sunday, this value will be 0 until the first Sunday of a month, where it will start with 1. (0 for April 1, 2020)

 [noncalendarWeekOfMonth] 18
 A numerical value counting weeks in a given month, with the first day of the month having a value of 1 regardless of when the month starts. (1 for April 1, 2020)

 [calendarWeekOfQuarter] 19 
 A numerical value counting full weeks in a given quarter. If a quarter starts on a day other than Sunday, this value will be 0 until the first Sunday of a quarter, where it will start with 1. (0 for April 1, 2020)

 [noncalendarWeekOfQuarter] 20
 A numerical value counting weeks in a given quarter, with the first day of the quarter having a value of 1 regardless of when the quarter starts. (1 for April 1, 2020)

 [calendarWeekOfYear] 21 
 A numerical value counting full weeks in a given year. If a year starts on a day other than Sunday, this value will be 0 until the first Sunday of a year, where it will start with 1. (13 for April 1, 2020)

 [noncalendarWeekOfYear] 22 
 A numerical value counting weeks in a given year, with the first day of the year having a value of 1 regardless of when the year starts. (14 for April 1, 2020)

 [yearQuarterMonthWeek] 23
 Same value as yearQuarterMonthWeekDay, albeit without the day as the last 2 digits (20202043 for April 15, 2020)

 [month] 24
 Numerical value for the given month (4 for April)

 [monthName] 25
 Name of the month (April for April)

 [monthOfQuarter] 26
 Numerical value counting months in a quarter. The first month of a quarter has a value of 1 (1 for April 1, 2020)

 [monthYear] 27 
 Date in the format of m/yyyy (4/2020 for April 1, 2020)

 [monthNameYear] 28 
 Date in the format of monthName, year (April, 2020 for April 1, 2020)

 [yearQuarterMonth] 29 
 Same value as yearQuarterMonthWeekDay, albeit without the week and day as the last 3 digits (2020204 for April 15, 2020)

 [termCode] 30 
 This is strange. Numerical value starting at 1 on January 1, 1900, incrementing up by 1 on May 11, July 1, August 21, and Jaunary 1 of the next year. So, 1/1/1900 has a value of 1, 5/11/1900 has a value of 2, 7/1/1900 has a value of 3, 8/21/1900 has a value of 4, 1/1/1901 has a value of 5, and the cycle continues. This is at least roughly aligned with our Spring (1/1-5/10), Summer I (5/10-6/30), Summer II (7/1-8/20), and Fall (8/20-12/31) terms

 [bannerTermCode] 31
 This is also strange. Numerical value composed of the year and then either 1,2,3, or 4 to denote the term. These seem to change with the markers denoted above, and are coded suce that 2 = Spring, 3 = Summer 1, 4 = Summer II, and 1 = Fall. So, 1/1/1900 has a value of 19002, 5/11/1900 has a value of 19003, 7/1/1900 has a value of 19004, 8/21/1900 has a value of 19001, 1/1/1901 has a value of 19012

 [termFrom1900] 32
 This is closer to common usage, but is still strange. First 4 digits are the year, last digit will always be 7. This has term identifiers like bannerTermCode, but this

time we're using a convention more used by TTU. These are coded suce that 5 = Spring, 8 = Summer 1, 9 = Summer II, and 2 = Fall. So, 1/1/1900 has a value of 190057, 5/11/1900 has a value of 190087, 7/1/1900 has a value of 190097, 8/21/1900 has a value of 190027, 1/1/1901 has a value of 190157.

 [quarter] 33
 Quarter of the year, value is 1,2,3 or 4 depending on if the current date is on or after January 1, April 1, July 1, and October 1

 [quarterName] 34
 Same numerical value as before, with a Q in front of it (Q2)

 [quarterYear] 35 
 Numerical value showing the quarter and year separated by a slash (2/2020)

 [quarterNameYear] 36 
 The quarterName and year separated by a space (Q2 2020)

 [yearQuarter] 37
 A 5 digit number with the first 4 digits being the year and the last digit being the quarter (20202 for Q2 2020)

 [year] 38
 The numerical value of the year (2020 for April 1, 2020)

 [quarterMonthWeekDay] 39
 yearQuarterMonthWeekDay value without the year as the first 4 digits (204315 for April 15, 2020)

 [quarterMonthWeek] 40 
 quarterMonthWeekDay value without the day as the last 2 digits (2043 for April 15, 2020)

 [quarterMonth] 41
 quarterMonthWeek without week as the last digit (204 for April 15, 2020) Y2iYbCJaLhbFPY7Yh

 [dayOfProcess] 42
 Numerical value counting days from the monday in the 3rd "calendarWeekOfMonth" in September. This date is labeled as "1" and counts up until the next such date of the next year. 9/16/2019 has value of 1, and counts up to 371 on 9/20/2020, as 9/21/2020 is the 3rd calendaryWeekofMonth Monday, and thus resets the count at 1. It seems this "3rd Wednesday" is being used as a "start Of Process" date for the following columns.

 [monthOfProcess] 43
 This is funky. This starts at 1 after the process start date identifed from "dayOfProcess" above. So, those dates in September
 will be listed as 1. This does not increment to 2 until calendarWeekOfMonth resets to 1 in October. Once calendarWeekOfMonth
 resets to 1 for the following September, this will have a value of "13" for all days before the next start of process date.

 [monthNameOfProcess] 44
 This is funky. This starts as "September" on the process start date used with dayOfProcess. It remains as "September" until calendarWeekOfMonth resets to 1, in which case it changes to "October". It will go back to "September" for "month 13".

 [monthWeekOfProcess] 45
 This is funky. A starting with the monthOfProcess value as the first 1-2 digits and ending with a modified calendarWeekOfMonth as the last 2 digits. Take for example the week that connects October 2019 - November 2019. The last 5 days of October have "calendarWeekOfMonth" of 4, while the first 2 days of November have a "calendarWeekOfMonth" of 0 (as "calendarWeekOfMonth isn't set to 1 until the first Sunday of a month). This "monthWeekOfProcess" column will use "4" for those 5 days in October and will use "5" for those first 2 days in November.

 [monthDayOfProcess] 46
 This is also funky. This is starts with the monthOfProcess value and ends with a value counting days within that month. In general, this counts days up from 1 whenever "monthOfProcess" resets to 1. However, this does not cleanly count up from 1 once we get to the end of the month and the start of a new month. It seems a formula for this column is based on the week calculated by "monthWeekOfProcess". Using our example before of October 2019 - November 2019: 10/31/2019 has an expected value of 226 (2nd "month of process", 26th day since the month started). The following day 11/1/2019 has a value of 234. I'm guessing the formula for this saw this was a Friday of Week 5 and said the day value must then be 34 (4 full weeks + 6 days = 34).

 [monthWeekDayOfProcess] 47
 This is monthWeekOfProcess with 2 digits at the end representing calendarDayOfWeek.

 [isLeapYear] 48
 A binary value stating 1 if the given date is part of a leap year.

 [processYear] 49 
 This is a 4 digit year representing the year of the fall term for which we are signing up students. Whenever we cross over past a new "start of process date"

(3rd Wednesday in September), this will increment by 1. For 9-16-2019, the "processYear" value is 2020, as on this date we are starting to sign people up for Fall 2020 housing. Once the date cycles around to the next "start of process date" on 9/21/2020, the year increments to 2021 (as we would have normally started signing up for Fall 2021 starting on/around that date).

 [startDateOfProcess] 50
 It looks like this is the date representing the monday in the 3rd "calendarWeekOfMonth" in September that is used as a basis for the previous columns (starting with "dayOfProcess").