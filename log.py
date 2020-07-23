from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("welcome")
window.geometry('350x200')
vtxtuname=StringVar()

def fnlogin():
    nm=str(vtxtuname.get())
    messagebox.showinfo("LoginInfo","Login successful"+nm)
#vtxtuname.set("Akash")

def fncancel():
    messagebox.showinfo("cancel Info","Quiting App")
    window.destroy

def Login(self):
        if lblname.get()==" " or lblpass.get()==" ":
            messagebox.showerror("Error","All fields are required!!")
        elif lblname.get()=="Akash" and lblpass.get()=="12345":
            messagebox.showinfo("Successful")
        else: 
            messagebox.showerror("Error","Invalid Username or Password")


lblname=Label(window,text='Username')
lblname.grid(row=0,column=0)
lblpass=Label(window,text='Password')
lblpass.grid(row=1,column=0)
txtuname=Entry(window,textvariable=vtxtuname)
txtuname.grid(row=0,column=1)
txtpass=Entry(window,show='*')
txtpass.grid(row=1,column=1)
b1=Button(text='LOGIN',command=fnlogin)
b2=Button(text='CANCEL',command=fncancel)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
            
window.mainloop()
