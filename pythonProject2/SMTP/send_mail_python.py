import smtplib

my_email = "kalashig333@gmail.com"
password = "vktb qbcy acjy vuzc"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email , password=password )
connection.sendmail(from_addr=my_email , to_addrs="ananygawande25@gmail.com", msg="subject:hell0\n\nquote")
connection.close()
