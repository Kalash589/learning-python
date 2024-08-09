import datetime as dt
import random
import smtplib

my_email = "kalashig333@gmail.com"
password = "vktb qbcy acjy vuzc"

now = dt.datetime.now()
current_day = now.weekday()

if current_day == 4:
    with open("quotes.txt") as qt:
        all_qoutes = qt.readlines()
        qoute = random.choice(all_qoutes)

    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(user=my_email , password=password)
        connection.sendmail(from_addr=my_email , to_addrs="rohan.ahire1166@gmail.com" , msg=f"subject:motivation\n\n {qoute}")
        