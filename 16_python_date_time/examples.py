from datetime import timedelta
from datetime import time
from datetime import date
from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print('\n')
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")


print("\n")
new_year = datetime(2025, 1, 1)
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one: ", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two: ", time_two)


# String to Time Using strptime -> change
print("\n")
date_string = "25 December, 2025"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date object =", date_object)


print("\n")
# Using data from datetime
d = date(2025, 1, 1)
print(d)
print("Current date:", d.today())
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

print("\n")
# Time Objects to Represent Time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

print("\n")
# Difference Between Two Points in Time Using
today = date(year=2025, month=12, day=25)
new_year = date(year=2026, month=1, day=1)
time_left_for_new_year = new_year - today
print("Time left for new year: ", time_left_for_new_year)

t1 = datetime(year=2025, month=12, day=25, hour=16, minute=1, second=50)
t2 = datetime(year=2026, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print("Time left for new year:", diff)

print("\n")
# Difference Between Two Points in Time Using timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
