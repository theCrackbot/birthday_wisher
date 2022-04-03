import datetime as dt
import random
import smtplib

my_email = "freetoxplor@gmail.com"
password = "Nsmskmdkmzk!1"

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="freetoxplor@yahoo.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")



