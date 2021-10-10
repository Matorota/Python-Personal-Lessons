import smtplib
import datetime as dt
import os, random
import pandas

# random_file = random.choice(os.listdir("C:\Users\Admin\Documents\GitHub\Nkkm-python\ 11-pask\ birthday-wisher\letter_templates"))

MY_EMAIL = "matumbarotas@gmail.com"
PASSWORD = "Bananas789#"

data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
bday = data[(data.month == today.month) & (data.day == today.day)]
name = bday["name"].tolist()
email = bday["email"].tolist()

PLACEHOLDER = "[]"

for n in range(len(name)):
    PLACEHOLDER.append(
        {
            "name": name[n],
            "email": email[n]
        }
    )
if not PLACEHOLDER:
    print("no birthday")
else:
    for name in PLACEHOLDER:
        num = random.randint(1, 3)
        with open(f"letter_templates/letter_{num}.txt") as letter:
            lines = letter.readlines()
            lines[0].strip()
            lines[0] = lines[0].replace("[NAME]", name["name"])
            message = "".join(lines)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=name["email"],
                                msg=f"Subject: HAPPY BIRTHDAY\n\n{message}")
            print(f"message sent to {name['name']}")


# def check_if_names_exists():
#     if os.path.exists(random_file):
#         print("names  found")
#         return True
#     else:
#         print("names not found")
#         return False


# with open(random_file) as file:
#     letter = file.read()
#     name = name()
#     new_letter = letter.replace(PLACEHOLDER, name)



# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="matumbarotas@gmail.com",
#         msg=f"Subject:Letter \n\n{new_letter}"
#     )

