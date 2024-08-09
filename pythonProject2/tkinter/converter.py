from tkinter import *

window=Tk()
window.title("converter")
window.minsize(200,100)

label1=Label(text="is equal to")
label1.grid(column=0, row=2)

label2=Label(text="miles")
label2.grid(column=2, row=1)

label3=Label(text="km")
label3.grid(column=2 , row=2)

entry=Entry(width=20)
print(entry.get())
entry.grid(column=1,row=1)

def convert():
    kms=int(entry.get())*2.1
    label4=Label(text=f"{kms}")
    label4.grid(column=1, row=2)


button=Button(text="Calculate" , command=convert)

button.grid(column=1 , row=3)

window.mainloop()
