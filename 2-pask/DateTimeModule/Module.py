# import datetime
# print(datetime.datetime.now())

from datetime import datetime
import  locale
locale.setlocale(locale.LC_TIME, "lt_LT")

print(datetime.now())

now = datetime.now()
concurrent_year = now.year
concurrent_month = now.month
concurrent_day = now.day
concurrent_hour = now.hour
concurrent_minute = now.minute
concurrent_secend = now.second
concurrent_weekday = now.weekday()

print(f"Year: \t\t{concurrent_year}")
print(f"month: \t\t{concurrent_month}")
print(f"day: \t\t{concurrent_day}")
print(f"hour: \t\t{concurrent_hour}")
print(f"minute: \t\t{concurrent_minute}")
print(f"second: \t\t{concurrent_secend}")
print(f"weekday: \t\t{concurrent_weekday}")

past = datetime(1990, 9, 29)
print(past.weekday())
future = datetime (year=2050, month=9, day =5)
print(future.weekday())


custom_date = f"Year: {now.strftime('%Y')}\n" \
              f"Month: {now.strftime('%B')}\n" \
              f"Weekday: {now.strftime('%A')}"

print(custom_date)
print(type(custom_date))
print(type(now.day))
print(type(now))






