
import datetime
# import pytz
d = datetime.date(2016,7,24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
print(tday.weekday())   ## Monday 0  -  Sunday 6
print(tday.isoweekday())  ## Monday 1  -  Sunday 7


tdelta  = datetime.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2025,1,22)
till_bday = bday - tday;
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

ttime = datetime.time(0,30,45,100000)

print(ttime.hour)
print(ttime.minute)
print(ttime.second)

dt = datetime.datetime(2016,7,26,12,30,45,100000)
print(dt.date())
print(dt.time())
print(dt.year)

tDelta = datetime.timedelta(days=7)
tDelta = datetime.timedelta(hours=12)
print(dt + tDelta)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)