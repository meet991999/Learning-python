import smtplib

my_email = "test11111.test1111@gmail.com"
password = "Thinkbig@meet"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="hackerearthmeet@gmail.com", msg="subject:hello\n\nthis is main text")
connection.close()
