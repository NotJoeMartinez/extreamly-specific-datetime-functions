import calendar
import datetime

def test(day):
    date = datetime.date(2019,1,1)
    
    c = calendar.Calendar(firstweekday=calendar.SUNDAY) 
    monthcal = c.monthdatescalendar(2019,1)
    today = datetime.date(2019,1,day)

    
    week_of_month = "error"

    if monthcal[0][0].month == today.month:
        start_index = 1 
    else:
        start_index = 0 

    for counter, week in enumerate(monthcal, start=start_index):
        if today in week and counter == 0:
            # get the max last week of month
            if today.month == 1:
                last_month = c.monthdatescalendar(today.year -1,12 )
            else:
                last_month = c.monthdatescalendar(today.year,today.month - 1)

            last_month_list = list(enumerate(last_month))
            week_of_month = last_month_list[-1][0]        
        else:
            week_of_month = counter

for i in range(1,30):
    print(test(i))



