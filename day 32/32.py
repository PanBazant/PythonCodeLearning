import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
month = now.month
day_of_week = now.weekday()
print(year)
print(month)
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)