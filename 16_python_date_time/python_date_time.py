""" Day 16: Python Date Time """

import datetime

print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")

# 1.1 Get the current day, month, year, hour, minute and timestamp
print("Question 1.1")
now = datetime.datetime.now()

print(f"Current day: {now.day}")
print(f"Current month: {now.month}")
print(f"Current year: {now.year}")
print(f"Current hour: {now.hour}")
print(f"Current minute: {now.minute}")
print(f"Current timestamp: {now.timestamp()}")

# 1.2 Format the current date
print("\nQuestion 1.2")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

# 1.3 Convert string date to datetime
print("\nQuestion 1.3")
date_string = "5 December 2019"
converted_date = datetime.datetime.strptime(date_string, "%d %B %Y")
print(converted_date)

# 1.4 Time difference between now and next new year
print("\nQuestion 1.4")
current_time = datetime.datetime.now()
next_new_year = datetime.datetime(year=current_time.year + 1, month=1, day=1)
time_diff_new_year = next_new_year - current_time
print(f"Time until New Year: {time_diff_new_year}")

# 1.5 Time difference between 1 January 1970 and now
print("\nQuestion 1.5")
epoch = datetime.datetime(1970, 1, 1)
time_diff_epoch = current_time - epoch
print(f"Time since 1 January 1970: {time_diff_epoch}")

# 1.6 Uses of datetime module
print("\nQuestion 1.6")
print("""
- Time series analysis
- Logging events with timestamps
- Scheduling tasks
- Blog post publishing dates
- Measuring execution time
""")
