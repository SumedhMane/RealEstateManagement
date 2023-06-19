

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

global label111
global cityIndex

global sqftvalue

def log():
    root.destroy()

class REM:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1150x700+0+0")
        self.root.resizable(0,0)
        # self.root.geometry("1350x700+0+0")

        self.root.title("Real Estate Management System")

        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root,text = "Real Estate Management System",image = self.icon_title,compound='left',font = ('times new roman',40,'bold'),bg="#010c48",fg='white',anchor='w' ,padx=20).place(relwidth = 1 , height = 70)

        #btn logout
        btn_logout = Button(self.root,text = 'Logout', font = ('times new roman', 15, 'bold'),bg='yellow',cursor='hand2',command=log).place(x=970,y=10,height =50,width=150 ) #x=1150

        self.lbl_clock=Label(self.root,font = ('times new roman',15),bg="#4d636d",fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth = 1 , height = 30)

        lbl1 = Label(self.root,text = " Enter Value from (400 - 3000) ",font = (('times new roman',14,'bold')),bg="#010c48",fg='white').place (x=585,y=150)
        lbl2 = Label(self.root,text = " Enter Area[In Sqfts] ",font = (('times new roman',20,'bold')),bg="#010c48",fg='white').place (x=180,y=210)
        lbl3 = Label(self.root,text = " Enter B.H.K ",font = (('times new roman',20,'bold')),bg="#010c48",fg='white').place (x=180,y=310)
        lbl4 = Label(self.root,text = " Choose Locality ",font = (('times new roman',20,'bold')),bg="#010c48",fg='white').place (x=180,y=410)

        lbl6 = Label(self.root,text = " Approxiamate Value ",font = (('times new roman',20,'bold')),bg="#010c48",fg='white').place (x=180,y=510)

root = Tk()
obj = REM(root)

sqftvalue = StringVar()
roomvalue = StringVar()
value11 = StringVar()

E1 = Entry(root,bg='powder blue',font=('Bodoni',22,'bold' ),textvariable=sqftvalue)
E1.place(x=580,y=205)

def onClick():
    lbl7= Label(root, text = "You have Entered 1 B.H.K ",font = ('helvatia', 14))
    lbl7.place(x=680 , y= 260)
    
def onClick1():
    lbl7= Label(root, text = "You have Entered 2 B.H.K ",font = ('helvatia', 14))
    lbl7.place(x=680 , y= 260)

def onClick2():
    lbl7= Label(root, text = "You have Entered 3 B.H.K ",font = ('helvatia', 14))
    lbl7.place(x=680 , y= 260)


btn1 = Button(root,bg='powder blue',font=('Bodoni',22,'bold' ),text = " 1 B.H.K ",width=5, command=onClick)
btn1.place(x=580,y=305)
btn2 = Button(root,bg='powder blue',font=('Bodoni',22,'bold' ),text = " 2 B.H.K ",width=5, command=onClick1)
btn2.place(x=700,y=305)
btn3 = Button(root,bg='powder blue',font=('Bodoni',22,'bold' ),text = " 3 B.H.K ",width=5, command=onClick2)
btn3.place(x=820,y=305)

def submit():
    sqft = sqftvalue.get()

    if sqft =="":
        messagebox.showerror("Error", " First Enter Sqft Value ")

    else:
        E9 = Label(root,bg='powder blue',font=('Bodoni',16,'bold' ),text = "Total Area (In Sqfts): ")
        E9.place(x=580,y=505)

        E8 = Label(root,bg='powder blue',font=('Bodoni',16,'bold' ))
        E8.config(text = sqft) 
        E8.place(x=820,y=505)

def resetall():
    root.destroy()
    import real_estate
    
    # sqftvalue.set("")
    # E8.config(text="")
    # E9.config(text="")
    # E11.set("")

btn5 = Button(root,bg='powder blue',font=('Bodoni',22,'bold' ),text = "Reset",width=20,command=resetall)
btn5.place(x=230,y=615)

btn6 = Button(root,bg='powder blue',font=('Bodoni',22,'bold' ),text = "Submit",width=20,command= submit)
btn6.place(x=660,y=615)

scroll = Scrollbar(root)

E3 = Listbox(root,bg='powder blue',font=('Bodoni',22,'bold' ), height = 2, yscrollcommand=scroll.set)
E3.place(x=580,y=405)

E3.insert(END,"1st block jayanagar")
E3.insert(END,"Ambedkar Nagar")
E3.insert(END,"2nd block jayanagar")
E3.insert(END,"Anandpura")
E3.insert(END,"Balagere")
E3.insert(END,"gottigere")
E3.insert(END,"banashankari")
E3.insert(END,"cv raman nagar")
E3.insert(END,"dasanapura")
E3.insert(END,"nagavarapalya")
E3.insert(END,"nehru nagar")
E3.insert(END,"sanjay nagar")
E3.insert(END,"sonnenahalli")
E3.insert(END,"shivaji nagar")
E3.insert(END,"thanisandra")
E3.insert(END,"yelahanka new town")
E3.insert(END,"yeshwanthpur")

scroll.pack( side = RIGHT, fill = Y )
scroll.config( command = E3.yview)



def getselecteditems():
    values = E3.curselection()
    if values:
        index = values[0]
        global val
        val = E3.get(index) #stores index
        E5 = Label(root,bg='powder blue',font=('Bodoni',16,'bold' ))
        E5.config(text = val) # preints location
        E5.place(x=790,y=535)

    E11 = Label(root,bg='powder blue',font=('Bodoni',16,'bold' ), text = "Your Location is : ")
    E11.place(x=580,y=535)

    E12 = Label(root,bg='powder blue',font=('Bodoni',16,'bold' ),text = "Price is : ")
    E12.place(x=580,y=565)

    dictt = {"0":
        {
            "Name": "1st block jayanagar",
            "Price" : "24 Lakhs",
        },
        "1": 
        {
            "Name": "Ambedkar Nagar",
            "Price" : "54 Lakhs",
        },
        "2" :
        {        
            "Name": "2nd block jayanagar",
            "Price" : "41 Lakhs",
        },
        "3" :
        {        
            "Name": "Anandpura",
            "Price" : "33 Lakhs",
        },
        "4" :
        {        
            "Name": "Balagere",
            "Price" : "12 Lakhs",
        },       
        
        "5" :
        {        
            "Name": "gottigere",
            "Price" : "19 Lakhs",
        },
        
        "6" :
        {        
            "Name": "banashankari",
            "Price" : "88 Lakhs",
        },
        "7" :
        {        
            "Name": "cv raman nagar",
            "Price" : "42 Lakhs",
        },    
        
        "8" :
        {        
            "Name": "dasanapura",
            "Price" : "69 Lakhs",
        },        
        
        "9" :
        {        
            "Name": "nagavarapalya",
            "Price" : "51 Lakhs",
        },        
        "10" :
        {        
            "Name": "nehru nagar",
            "Price" : "34.50 Lakhs",
        },        
        "11" :
        {        
            "Name": "sanjay nagar",
            "Price" : "71 Lakhs",
        },

        "12" :
        {        
            "Name": "sonnenahalli",
            "Price" : "93 Lakhs",
        },

        "13" :
        {        
            "Name": "shivaji nagar",
            "Price" : "57 Lakhs",
        },        
        "14" :
        {        
            "Name": "thanisandra",
            "Price" : "92 Lakhs",
        },       
        "15" :
        {        
            "Name": "yelahanka new town",
            "Price" : "56 Lakhs",
        },       
        "16" :
        {        
            "Name": "yeshwanthpur",
            "Price" : "13 Lakhs",
        },         

    }
    for key, value in dictt.items():
        if value["Name"] == val:
            i=key
            break

    E13 = Label(root,bg='powder blue',font=('Bodoni',16,'bold' ))
    E13.config(text =dictt[i]["Price"])
    E13.place(x=690,y=565)

btn6 = Button(root,bg='powder blue',font=('Bodoni',18 ),width=9,text = "Click",command= getselecteditems)
btn6.place(x=910,y=430)

root.mainloop()
