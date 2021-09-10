from datetime import datetime, date
#3uzduotis
past_date = datetime(2020, 5, 6)
today_date = datetime.now()
atsakymukas = today_date - past_date
print(atsakymukas.days)