import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekDay = now.weekday()

MY_EMAIL = "matumbarotas@gmail.com"
PASSWORD = "Bananas789#"
if weekDay == 6:
    with open("quotes.txt.", "r") as f:
     read = f.readlines()
     quote = random.choice(read)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="matumbarotas@gmail.com",
            msg=f"Subject:Monday motivation\n\n{quote}"
        )


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="matumbarotas@gmail.com",
#         msg=f"Subject:Hello from bum\n\n{f.read}"
#     )



