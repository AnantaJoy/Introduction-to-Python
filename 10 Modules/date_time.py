from datetime import datetime

now = datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# arithmetic with dates
from datetime import timedelta

today = datetime.now()
print("Today is: " + str(today))

one_day = timedelta(days=1)
yesterday = today - one_day
print("Yesterday was: " + str(yesterday))

one_week = timedelta(weeks=1)
next_week = today + one_week
print("Next week is: " + str(next_week))

# formatting dates
from datetime import datetime

today = datetime.now()
print("Today is: " + str(today))

# dd/mm/YY H:M:S
print(today.strftime("%d/%m/%Y %H:%M:%S"))
print(today.strftime("%d/%m/%Y %I:%M:%S %p"))

# dd-mm-YY H:M:S
print(today.strftime("%d-%m-%Y %H:%M:%S"))

# 