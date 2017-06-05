from datetime import datetime

# now = datetime.now()
# print(now)
print(datetime.now())

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
print(current_year)
print(current_month)
print(current_day)
print("Today is %s/%s/%s" % (current_month, current_day, current_year))

current_hour = now.hour
current_minute = now.minute
current_second = now.second
print(current_hour)
print(current_minute)
print(current_second)
print("Time is %s:%s:%s" % (current_hour, current_minute, current_second))

print("Currently it's %s/%s/%s %s:%s:%s" % (current_month, current_day, current_year,current_hour, current_minute, current_second))