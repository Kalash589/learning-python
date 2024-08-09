import json
from tkinter import *
from tkinter import messagebox
from random import random,shuffle,randint,choice
import pyperclip
FONT_NAME = "Aerial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    symbols=['!','#','$','%',' &','*','+']

    nr_letters=randint(8,10)
    nr_numbers=randint(2,4)
    nr_symbols=randint(2,4)

    password_list0=[choice(letters) for char in range(nr_letters)]
    password_list1 = [choice(numbers) for num in range(nr_numbers)]
    password_list2= [choice(symbols) for sym in range(nr_symbols)]

    password_list=password_list0 + password_list2 + password_list1
    shuffle(password_list)

    password="".join(password_list)
    print(password)
    Password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    username=Username_entry.get()
    password=Password_entry.get()
    new_data={
        website:{
            "Email":username ,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Ooops", message="Please do not leave any filed Empty")
    else:
        try:
            with open ("data.json" , "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)

            with open("data.json" , "w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            Password_entry.delete(0,END)

def search():
    website=website_entry.get()
    try:
        with open("data.json") as data_files:
            data=json.load(data_files)

    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="Data not found")

    else:
         if website in data:
            email=data[website]["Email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website , message=f"your data is as follow:\nEmail:{email}\n Password:{password}")
         else :
             messagebox.showinfo(title=Error, message=f"No details for {website} found!!")





# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Generator")
window.minsize(600,400)

window.config(padx=50,pady=50,bg="black")

canvas=Canvas(width=200, height=190 , highlightthickness=0, bg="black")
logo_pic=PhotoImage(file="logo.png")
canvas.create_image(100,100 ,image=logo_pic)
canvas.grid(column=1 , row = 0)

website_label=Label(text="Website:" ,font=(FONT_NAME,15) , fg="white" , bg="black")
website_label.grid(column=0 , row=1)

username_label=Label(text="Username:" ,font=(FONT_NAME,15) , fg="white" , bg="black")
username_label.grid(column=0 , row=2)

Password_label=Label(text="Password:" ,font=(FONT_NAME,15) , fg="white" , bg="black")
Password_label.grid(column=0 , row=3)

website_entry=Entry(width=21,fg="white", bg="grey" ,bd=1, highlightthickness=0,)
website_entry.grid(column=1,row=1 , columnspan=1)
website_entry.focus()


Username_entry=Entry(width=36,fg="white", highlightthickness=0,bg="grey")
Username_entry.insert(0,"kalash@gmail.com")
Username_entry.grid(column=1,row=2 , columnspan=2)

Password_entry=Entry(width=21,fg="white", highlightthickness=0,bg="grey")
Password_entry.grid(column=1,row=3 )

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2 , row =3)

Add_button=Button(text="Add", width=36 , highlightthickness=0 , command=save)
Add_button.grid(column=1 , row =4,columnspan=2)

search_button=Button(text="Search",width=12, command=search)
search_button.grid(column=2,row=1)


window.mainloop()