
from tkinter import *
from tkinter import messagebox
import mysql.connector

def loginuser():
    username=user.get()
    password=passwd.get()

    if (username=="" or username=="User_ID") or (password=="" or password == "Password"):
        messagebox.showerror("Entry Error","Type Correct Username And Password")

    else:
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',password='Nandini@1966',database="studentregistration")
            mycursor=mydb.cursor()
            print("Connected to Database Successfull !!")

        except:
            messagebox.showerror("Connection","Database Not Connected")
            return

        command="use studentregistration"
        mycursor.execute(command)

        command="select * from login where Username=%s and Password = %s"
        mycursor.execute(command,(username,password))
        myresult=mycursor.fetchone()
        print(myresult)

        if myresult == None:
            messagebox.showinfo("Invalid","Invalid User-ID and Password")

        else:
            messagebox.showinfo("Login","Successfully Logged In")
            root.destroy()

        
root=Tk()

root.title("Login System")
root.geometry("1250x700")
root.config(bg="#06283D")
root.resizable(False,False)

#icon image
image_icon=PhotoImage(file="login_images/icon.png")
root.iconphoto(False,image_icon)

#background image

frame= Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimg=PhotoImage(file="login_images/LOGIN.png")
Label(frame,image=backgroundimg).pack()

# userEnrty
def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    name = user.get()
    if name =='':
        user.insert(0, 'User_ID')

user = Entry(frame,width=10,fg="#fff",border=0,bg="#375174",font=('times new roman',20))
user.insert(0, 'User_ID')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x=500,y=315)

# PasswordEnrty
def password_enter(e):
    passwd.delete(0,'end')

def password_leave(e):
    if passwd.get() =="":
        passwd.insert(0, 'Password')

passwd = Entry(frame,width=10,fg="#fff",border=0,bg="#375174",font=('times new roman',20))
passwd.insert(0, 'Password')
passwd.bind("<FocusIn>",password_enter)
passwd.bind("<FocusOut>",password_leave)
passwd.place(x=500,y=410)

#hide and show button

button_mode=True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeye,activebackground="white")
        passwd.config(show="*")
        button_mode=False

    else:
        eyeButton.config(image=openeye,activebackground="white")
        passwd.config(show="")
        button_mode=True

openeye=PhotoImage(file="login_images/openeye.png")
closeye=PhotoImage(file="login_images/close_eye.png")

eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=780,y=410)


loginbut1=Button(root,text="LOGIN",bg="#1f5675",fg='white',width=10,height=1,font=('times new roman',16,'bold'),command=loginuser)
loginbut1.place(x=570,y=600)


root.mainloop()

