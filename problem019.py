#Project Euler Problem #019: Counting Sundays
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31. Dec 2000)
#Leap years: every for year except on a century unless its divisible by 400

def daysOfMonth(mon, year):
    monthDays = {0:31, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}
    if mon != 1:
       return monthDays[mon]
    elif mon == 1 and year % 4 == 0 and ((year % 100 != 0) != (year % 400 == 0)):
        return 29
    else:
        return 28

def daysTillStart(day, mon, year):
    yearShort = year - 1900
    days = 0
    for i in range(yearShort):
        if daysOfMonth(1, i + 1900) == 28:
            days += 365
        else:
            days += 366
    for j in range(mon):
        days += daysOfMonth(j, year)
    days += day
    return days
def test(i):
    for year in range(i):
        for month in range(12):
            for day in range(daysOfMonth(month, year + 1900)):
                print(daysTillStart(day, month, year + 1900))
#print(daysTillStart(0, 0, 1900))
print(daysOfMonth(1, 2000)) 
#days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
count = 0
for i in range(1901, 2001): 
    for j in range(12):
        if daysTillStart(0, j, i) % 7 == 6:
            count += 1
print(count)
#test(2)
