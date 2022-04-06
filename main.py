import datetime as dt
from random import choice
import smtplib

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

curr_date = dt.datetime.now()
week_day_index = curr_date.weekday()

if curr_date.weekday() == 0:

    with open("quotes.txt") as quotes:
        list_of_quotes = quotes.readlines()
        random_quote = choice(list_of_quotes)

    email_sender = "patryktester5@yahoo.com"
    email_recipient = "bzdura5@gmail.com"
    email_password = "jgxjyyvchnanomwv"
    host = "smtp.mail.yahoo.com"
    subject = f"Subject:Have a great {days_of_the_week[week_day_index]}\n\n"
    body = random_quote

    with smtplib.SMTP(host=host) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=email_password)
        connection.sendmail(
            from_addr=email_sender,
            to_addrs=email_recipient,
            msg=subject + body
        )
