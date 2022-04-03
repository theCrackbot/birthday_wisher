import smtplib

my_email = "freetoxplor@gmail.com"
password = "Nsmskmdkmzk!1"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs="freetoxplor@yahoo.com",
                    msg="Subject:Hello\n\nThis is a test mail.")
connection.close()