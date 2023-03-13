import smtplib

my_email = "mail@gmail.com"
password = "abcd1234()"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="test@gmail.com", msg="Subject:Hello\n\nThis is the body of my email.") # trzeba dać dwa znaki nowej linii by przejśc do treści
connection.close()
