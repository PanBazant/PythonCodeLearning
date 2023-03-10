from calendar import weekday
import smtplib
import datetime as dt
import random

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "test"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("day 32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smt.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}")
