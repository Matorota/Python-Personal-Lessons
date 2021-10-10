import smtplib

MY_EMAIL = "matumbarotas@gmail.com"
PASSWORD = "Bananas789#"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs = "matumbarotas@gmail.com",
        msg="Subject:Hello from py\n\nHello, this is pythpn code"
    )
