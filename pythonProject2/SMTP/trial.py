mport smtplib
import datetime as dt
import pandas

now = dt.datetime.now()
current_month = now.month
current_day = now.day

my_email = "kalashig333@gmail.com"
password =  "vktb qbcy acjy vuzc"

with open("birthday_date.csv" , "r") as dates:
    all_dates = pandas.read_csv(dates)
    date_table = pandas.DataFrame(all_dates)
    print(all_dates)
    for idx,row in date_table.iterrows():
        if row[month] == current_month and row[day] == current_day:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email , password=password)
                connection.sendmail(from_addr=my_email , to_addrs=)
