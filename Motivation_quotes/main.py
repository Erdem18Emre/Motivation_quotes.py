import smtplib
import datetime as dt
import random

# Your information

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "your password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readline()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation \n\n{quote}"
                            )

