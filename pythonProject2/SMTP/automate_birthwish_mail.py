import smtplib
import datetime as dt
import pandas

today = dt.datetime.now()
today_tuple = (today.month , today.day)

my_email = "kalashig333@gmail.com"
password = "vktb qbcy acjy vuzc"


data = pandas.read_csv("birthday_date.csv")
birthday_dict = {(data_row["month"] , data_row["day"]) : data_row for (index,data_row) in data.iterrows()}
birthday_name = birthday_dict[today_tuple]["name"]

if today_tuple in birthday_dict:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email , password=password)
        print(f"subject:Birthday wish \n\n To dear {birthday_name} \n Happiest birthday to you!!")
        connection.sendmail(from_addr=my_email , to_addrs=birthday_dict[today_tuple]["mail"] , msg=f"subject:Birthday wish \n\n To dear {birthday_name} \n Happiest birthday to you!!")

else:
    pass






