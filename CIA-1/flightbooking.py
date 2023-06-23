from tkinter import *
from tkinter.messagebox import *
import sqlite3
root=Tk()
root.title("Home Page")
con=sqlite3.Connection('flight_db')
cur=con.cursor()
cur.execute("create table if not exists airlines(user_name varchar(20) primary key,first_name varchar(20),last_name varchar(20),phone_number number(10),email varchar(30),passw varchar(20))")

LARGEFONT =("Bookman Old Style", 20)
MEDFONT = ("Lucida Handwriting", 15)
TEXT = ("Verdana", 10)

fr2=Frame()
fr2.pack()
label = Label(fr2,text ="Welcome to Lavasa Airlines, What do you want to do?", font = LARGEFONT)
label1 = Label(fr2,text="** The official airlines of Lavasa **", font = MEDFONT)
blank = Label(fr2,text=" ", font = MEDFONT)

label.grid(row = 1)
label1.grid(row = 2)
blank.grid(row = 3)
class startpage():
    def airline():
        root.destroy()
        root1=Tk()
        root1.title("Booking Portal")
        Label(root1,text="Welcome to Lavasa Airlines",font=("Baskerville Old Face",17),width=46,bg="White").grid(row=0,column=0,columnspan=4)
        Label(root1,text="Flights Availability",font=("Baskerville Old Face",17),width=46).grid(row=1,column=0,columnspan=4)
        Label(root1,text="Select Pick Up Point",font=("Baskerville Old Face",14),fg="Crimson").grid(row=2,column=1)
        variable = StringVar(root1)
        variable.set("Select Source") # default value
        w = OptionMenu(root1, variable, "Goa", "Chennai", "Lavasa","Maldives","Melbourne")
        w.grid(row=2,column=2)
        Label(root1,text="Select Boarding Point",font=("Baskerville Old Face",14),fg="Blue").grid(row=3,column=1)
        variable1 = StringVar(root1)
        variable1.set("Select Destination") # default value
        w = OptionMenu(root1, variable1, "Goa", "Chennai", "Lavasa","Maldives","Melbourne")
        w.grid(row=3,column=2)
        #Sign In
        def signup():
                     def success():
                        user = user_name.get()
                        cur.execute("select user_name from airlines where user_name=(?)", (user,))
                        a = cur.fetchall()
                        if a != []:
                              showerror('Error',"Username Already Exists")
                        else:
                              l = (user_name.get(), first_name.get(), last_name.get(),phone_number.get(),email.get(), passw.get())
                                cur.execute("insert into airlines values(?,?,?,?,?,?)",l)
                                showinfo('Signed Up',"Congratulation You are Successfully Signed Up")
                                con.commit()
                                user_name.delete(0,20)
                                first_name.delete(0,20)
                                last_name.delete(0,20)
                                phone_number.delete(0,10)
                                email.delete(0,30)
                                passw.delete(0,20)
                                root1.destroy()
                                root=Tk()
                                root.title("Sign Up")
                                Label(root,text="Welcome to Lavasa Airlines",font=("Baskerville Old Face",17),width=46,bg="White").grid(row=0,column=0,columnspan=4)
                                Label(root,text="Sign Up",font=("Baskerville Old Face",17),width=46,bg="Black", fg = "white").grid(row=1,column=0,columnspan=4)
                                Label(root,text="Username*",font=("Baskerville Old Face",14),fg="darkslategrey").grid(row=2,column=1)
                                user_name=Entry()
                                user_name.grid(row=2,column=2)
                                Label(root,text="First Name",font=("Baskerville Old Face",14),fg="darkslategrey").grid(row=3,column=1)
                                first_name=Entry()
                                first_name.grid(row=3,column=2)
                                Label(root,text="Last Name",font=("Baskerville Old Face",14),fg="darkslategrey").grid(row=4,column=1)
                                last_name=Entry()
                                last_name.grid(row=4,column=2)
                                Label(root,text="Phone Number",font=("Baskerville Old Face",14),fg="darkslategrey").grid(row=5,column=1)
                                phone_number=Entry()
                                phone_number.grid(row=5,column=2)
                                Label(root,text="Email",font=("Baskerville Old Face",14),fg="darkslategrey").grid(row=6,column=1)
                                email=Entry(width=30)
                                email.grid(row=6,column=2)
                                Label(root,text="Password*",font=("Baskerville Old Face",14),fg="darkslategrey").grid(row=7,column=1)
                                passw=Entry(root,show="*")
                                passw.grid(row=7,column=2)
                                Button(root,text="Sign up",font=("Comic Sans MS",10),command=lambda: success()).grid(row=8,columnspan=5)
                        def signin():
                            root.destroy()
                            root2=Tk()
                            root2.title("Sign In")
                            Label(root2,text="Welcome to Airplane Booking System",font=("Baskerville Old Face",17),width=46,bg="White").grid(row=0,column=0,columnspan=4)
                            Label(root2,text="Sign In",font=("Baskerville Old Face",17),width=46).grid(row=1,column=0,columnspan=4)
                            Label(root2,text="Username*",font=("Baskerville Old Face",14),fg="maroon").grid(row=2,column=1)
                            user_name=Entry()
                            user_name.grid(row=2,column=2)
                            Label(root2,text="Password*",font=("Baskerville Old Face",14),fg="maroon").grid(row=3,column=1)
                            passw=Entry(root2,show="*")
                            passw.grid(row=3,column=2)
                        def bookingportal():
                              usr = user_name.get()
                                passs = passw.get()
                                cur.execute("select * from airlines where user_name=(?) and passw=(?)", (usr, passs,))
                                a = cur.fetchall()
                                if a==[]:
                                    showerror('Log In Failed', "Invalid Username or Password")
                                else:
                                    root2.destroy()
                                    root4=Tk()
                                    root4.title("Booking Portal")
                                    Label(root4,text="Welcome to Airplane Booking System",font=("Baskerville Old Face",17),width=46,bg="White").grid(row=0,column=0,columnspan=4)
                                    Label(root4,text="Booking Portal",font=("Baskerville Old Face",17),width=46).grid(row=1,column=0,columnspan=4)
                                    Label(root4,text="Enter Your Details",font=("Baskerville Old Face",14),fg="maroon",width=46).grid(row=2,column=0,columnspan=4)
                                    Label(root4,text="Full Name",font=("Sitka Subheading Semibold",14),fg="maroon").grid(row=3,column=1)
                                    name=Entry()
                                    name.grid(row=3,column=2)
                                    Label(root4,text="Enter Your age",font=("Sitka Subheading Semibold",14),fg="maroon").grid(row=4,column=1)
                                    age=Entry(width=4)
                                    age.grid(row=4,column=2)
                                    Label(root4,text="Select Gender",font=("Sitka Subheading Semibold",14),fg="maroon").grid(row=5,column=1)
                                    a=IntVar()
                                    Radiobutton(root4,text="Male",variable=a,value=0,fg="red").grid(row=5,column=2)
                                    Radiobutton(root4,text="Female",variable=a,value=1,fg="orchid").grid(row=5,column=3)
                                    Label(root4,text="Seat Class",font=("Sitka Subheading Semibold",14),fg="blue").grid(row=6,column=1)
                                    v= StringVar(root4)
                                    v.set("Select class") # default value
                                    w = OptionMenu(root4, v, "First Class", "Business Class", "Economy Class")
                                    w.grid(row=6,column=2)
                                    Label(root4,text="Additional Passengers Details",font=("Sitka Subheading Semibold",14),fg="Blue",width=46).grid(row=7,column=0,columnspan=4)
                                    Label(root4,text="Passenger 1",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=8,column=1)
                                    name1=Entry()
                                    name1.grid(row=8,column=2)
                                    Label(root4,text="Enter age",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=9,column=1)
                                    age1=Entry(width=4)
                                    age1.grid(row=9,column=2)
                                    Label(root4,text="Seat Class",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=10,column=1)
                                    v1= StringVar(root4)
                                    v1.set("Select class") # default value
                                    w1 = OptionMenu(root4, v1, "First Class", "Business Class", "Economy Class")
                                    w1.grid(row=10,column=2)
                                    Label(root4,text="Passenger 2",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=11,column=1)
                                    name2=Entry()
                                    name2.grid(row=11,column=2)
                                    Label(root4,text="Enter age",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=12,column=1)
                                    age2=Entry(width=4)
                                    age2.grid(row=12,column=2)
                                    Label(root4,text="Seat Class",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=13,column=1)
                                    v2= StringVar(root4)
                                    v2.set("Select class") # default value
                                    w2 = OptionMenu(root4, v2, "First Class", "Business Class", "Economy Class")
                                    w2.grid(row=13,column=2)
                                    Label(root4,text="Passenger 3",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=14,column=1)
                                    name3=Entry()
                                    name3.grid(row=14,column=2)
                                    Label(root4,text="Enter age",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=15,column=1)
                                    age3=Entry(width=4)
                                    age3.grid(row=15,column=2)
                                    Label(root4,text="Seat Class",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=16,column=1)
                                    v3= StringVar(root4)
                                    v3.set("Select class") # default value
                                    w3 = OptionMenu(root4, v3, "First Class", "Business Class", "Economy Class")
                                    w3.grid(row=16,column=2)
                                    Label(root4, text="Journey Date:",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=17,column=1)
                                    date = Entry(root4, width=15, font=("Sitka Subheading Semibold", 14),fg="darkolivegreen")
                                    date.grid(row=17, column=2)
                                    date.insert(0,"DD/MM/YYYY")
                                    Label(root4,text="Number of Passengers",font=("Sitka Subheading Semibold",14),fg="darkolivegreen").grid(row=18,column=1)
                                    v4= StringVar(root4)
                                    v4.set("0") # default value
                                    w4 = OptionMenu(root4, v4, "1", "2", "3","4")
                                    w4.grid(row=18,column=2)
                                    def data():
                                            root5=Tk()
                                            root5.title("Ticket Details")
                                            Label(root5,text="Thanks For Choosing Airplane Booking System",font=("Sitka Subheading Semibold",17),width=46).grid(row=0,column=0,columnspan=4)
                                            Label(root5,text="Ticket Details",font=("Sitka Subheading Semibold",17),fg="indigo",width=46).grid(row=1,column=0,columnspan=4)
                                            Label(root5,text="Passenger Name",font=("Century Schoolbook",14),fg="indigo").grid(row=2,column=1)
                                            Label(root5,text=name.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=2,column=2)
                                            Label(root5,text="Age",font=("Century Schoolbook",14),fg="indigo").grid(row=3,column=1)
                                            Label(root5,text=age.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=3,column=2)
                                            Label(root5,text="Gender",font=("Century Schoolbook",14),fg="indigo").grid(row=4,column=1)
                                            if(a.get()==0):
                                                    Label(root5,text="Male",font=("Century Schoolbook",14),fg="indigo").grid(row=4,column=2)
                                            else:
                                                    Label(root5,text="Female",font=("Century Schoolbook",14),fg="indigo").grid(row=4,column=2)
                                            Label(root5,text="Class",font=("Century Schoolbook",14),fg="indigo").grid(row=5,column=1)
                                            Label(root5,text=v.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=5,column=2)
                                            Label(root5,text="Date",font=("Century Schoolbook",14),fg="indigo").grid(row=6,column=1)
                                            Label(root5,text=date.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=6,column=2)
                                            Label(root5,text="Additional Passenger Details",font=("Baskerville Old Face",17),fg="indigo",width=46).grid(row=7,column=0,columnspan=4)
                                            Label(root5,text="Passenger Name",font=("Century Schoolbook",14),fg="indigo").grid(row=8,column=1)
                                            Label(root5,text=name1.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=8,column=2)
                                            Label(root5,text="Class",font=("Century Schoolbook",14),fg="indigo").grid(row=9,column=1)
                                            Label(root5,text=v1.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=9,column=2)
                                            Label(root5,text="Passenger Name",font=("Century Schoolbook",14),fg="indigo").grid(row=10,column=1)
                                            Label(root5,text=name2.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=10,column=2)
                                            Label(root5,text="Class",font=("Century Schoolbook",14),fg="indigo").grid(row=11,column=1)
                                            Label(root5,text=v2.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=11,column=2)
                                            Label(root5,text="Passenger Name",font=("Century Schoolbook",14),fg="indigo").grid(row=12,column=1)
                                            Label(root5,text=name3.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=12,column=2)
                                            Label(root5,text="Class",font=("Century Schoolbook",14),fg="indigo").grid(row=13,column=1)
                                            Label(root5,text=v3.get(),font=("Century Schoolbook",14),fg="indigo").grid(row=13,column=2)
                                            Label(root5,text="Amount Per Passsenger",font=("Baskerville Old Face",17),fg="indigo",width=46).grid(row=14,column=0,columnspan=4)
                                            Label(root5,text="Ticket From " + variable.get() + "<-> to <->" + variable1.get(),bg="lightcoral",font=("Times New Roman",10),width=46).grid(row=15,column=0,columnspan=4)
                                            def amount(price):

                                                    if (int(v4.get())==1):
                                                        print (v.get())
                                                    if(v.get()=="First Class"):
                                                        price=10000

                                                    elif (v.get()=="Business Class"):
                                                        price=6000
                                                    elif(v.get()=="Econoy Class"):
                                                        price=3800
                                                    elif int(v4.get())==2:
                                                        if(v.get()=="First Class" and v1.get()=="First Class"):
                                                            price=20000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class"):
                                                            price=16000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class"):
                                                            price=13800
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class"):
                                                            price=16000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class"):
                                                            price=12000
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class"):
                                                            price=9800
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class"):
                                                            price=13800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class"):
                                                            price=9800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class"):
                                                            price=7600
                                                    elif (int(v4.get())==3):
                                                        if(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                            price=30000
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                            price=26000
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                             price=23800
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                            price=30000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                            price=26000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                             price=23800
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                            price=30000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                            price=26000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                             price=23800
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                            price=26000
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                            price=22000
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                             price=19800
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                            price=22000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                             price=18000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                             price=15800
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                             price=19800
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                            price=15800
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                             price=13600
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                            price=23800
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                            price=19800
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                             price=17600
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                            price=19800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                            price=15800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                             price=13600
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                            price=17600
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                            price=13600
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                             price=11400
                                                             Label(root5,text="Price",font=("Century Schoolbook",14),fg="goldenrod").grid(row=16,column=1)
                                                             Label(root5,text=price,font=("Century Schoolbook",14),fg="goldenrod").grid(row=16,column=2)
                                                             Label(root5,text="Total Amount",font=("Century Schoolbook",14),fg="goldenrod").grid(row=18,column=1)
                                                             Label(root5,text=price*int(v4.get()),font=("Century Schoolbook",14),fg="goldenrod").grid(row=18,column=2)
                                                    elif (int(v4.get())==4):
                                                        if(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                            price=40000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                            price=36000
                                                        elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                            price=33800
                                                    Label(root5,text="Price",font=("Century Schoolbook",14),fg="Blue").grid(row=16,column=1)
                                                    Label(root5,text=price,font=("Century Schoolbook",14),fg="Blue").grid(row=16,column=2)
                                                    Label(root5,text="Total Amount",font=("Century Schoolbook",14),fg="Blue").grid(row=18,column=1)
                                                    Label(root5,text=price*int(v4.get()),font=("Century Schoolbook",14),fg="Blue").grid(row=18,column=2)
                                            Button(root5,text="Price",font=("Times New Roman"),command=amount(0)).grid(row=20,columnspan=5)
                                            Label(root5,text="Number of Passengers",font=("Century Schoolbook",14),fg="Blue").grid(row=17,column=1)
                                            Label(root5,text=v4.get(),font=("Century Schoolbook",14),fg="Blue").grid(row=17,column=2)
                                            def exitw():
                                                root4.destroy()
                                                root5.destroy()
                                            Button(root5,text="Done",font=("Times New Roman"),command=exitw).grid(row=19,columnspan=5)

                                            Button(root4,text="Confirm Booking",font=("algerian"),command=data).grid(row=19,columnspan=5)
                                            Button(root2,text="Sign In",font=("Britannic Bold",10),command=lambda: bookingportal()).grid(row=4,columnspan=5)
                                            Button(root,text="Sign in",font=("Britannic Bold",10),command=signin).grid(row=9,columnspan=5)

        def flights():
            if variable.get()=="Goa" and variable1.get()=="Chennai":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="100",font=("Baskerville Old Face",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Goa" and variable1.get()=="Lavasa":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="250",font=("Baskerville Old Face",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Goa" and variable1.get()=="Maldives":
                showerror('Oops!',"Sorry No direct flights available for this root")
            if variable.get()=="Goa" and variable1.get()=="Melbourne":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="201",font=("Bookman Old Style",14),bg="green").grid(row=4,columnspan=5,column=2)
            if variable.get()=="Chennai" and variable1.get()=="Goa":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="100",font=("Baskerville Old Face",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Chennai" and variable1.get()=="Lavasa":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="150",font=("Baskerville Old Face",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Chennai" and variable1.get()=="Maldives":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="115",font=("Baskerville Old Face",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Chennai" and variable1.get()=="Melbourne":
                showerror('Oops!',"Sorry No direct flights available for this root")
            if variable.get()=="Lavasa" and variable1.get()=="Goa":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="250",font=("Baskerville Old Face",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Lavasa" and variable1.get()=="Chennai":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="150",font=("Bookman Old Style",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Lavasa" and variable1.get()=="Maldives":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="167",font=("Bookman Old Style",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Lavasa" and variable1.get()=="Melbourne":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="160",font=("Baskerville Old Face",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Maldives" and variable1.get()=="Goa":
                showerror('Oops!',"Sorry No direct flights available for this root")
            if variable.get()=="Maldives" and variable1.get()=="Lavasa":
                Label(root1,text="Number of Seats Available are:",font=("Baskerville Old Face",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="167",font=("Baskerville Old Face",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Maldives" and variable1.get()=="Chennai":
                Label(root1,text="Number of Seats Available are:",font=("Bookman Old Style",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="115",font=("Bookman Old Style",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Maldives" and variable1.get()=="Melbourne":
                Label(root1,text="Number of Seats Available are:",font=("Bookman Old Style",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="168",font=("Bookman Old Style",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Melbourne" and variable1.get()=="Goa":
                Label(root1,text="Number of Seats Available are:",font=("Bookman Old Style",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="201",font=("Bookman Old Style",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Melbourne" and variable1.get()=="Lavasa":
                Label(root1,text="Number of Seats Available are:",font=("Bookman Old Style",14),bg="orange").grid(row=5,columnspan=4)
                Label(root1,text="160",font=("Bookman Old Style",14),bg="green").grid(row=5,columnspan=4,column=2)
            if variable.get()=="Melbourne" and variable1.get()=="Chennai":
               showerror('Oops!',"Sorry No direct flights available for this root")
            if variable.get()=="Melbourne" and variable1.get()=="Maldives":
                Label(root1,text="Number of Seats Available are:",font=("Bookman Old Style",14),bg="black").grid(row=5,columnspan=4)
                Label(root1,text="168",font=("Bookman Old Style",14),bg="black").grid(row=5,columnspan=4,column=2)
            Button(root1,text="Signup to Book",bg="black",font=("Britannic Bold",10),command=signup).grid(row=7,columnspan=5)
        Button(root1,text="Show Flights",font=("Britannic Bold",10),bg="black",compound="center",command=flights).grid(row=6,columnspan=1)
        root1.mainloop()

    def flights_av():
        root.withdraw()
        root1=Tk()
        root1.title("Flights Available")

        label = Label(root1, text ="Destinations", font = LARGEFONT)

        label.grid(row = 1)


        def maldives():
            root1.withdraw()
            root2=Tk()
            root2.title("Maldives")
            label = Label(root2, text ="Maldives", font = LARGEFONT)
            label.grid(row = 1)

            info = Label(root2, text ="Maldives, officially the Republic of Maldives, is a small archipelagic state in South Asia, situated in the Arabian Sea of the Indian Ocean. It lies southwest of Sri Lanka and India, about 700 kilometres from the Asian continent's mainland", font = TEXT)
            info.grid(row = 2)

            blank = Label(root2, text =" ", font = TEXT)
            blank.grid(row = 3)

            time = Label(root2, text ="AVALIABLE FLIGHT TIME: 4 AM, 1 PM, 7 PM", font = TEXT)
            time.grid(row = 4)

            price = Label(root2, text ="PRICE: 10000 Rs, 6000 Rs, 3800 Rs", font = TEXT)
            price.grid(row = 5)

            button2 = Button(root2, text ="Book a flight",  width = 75,
            command = startpage.airline)
            button2.grid(row = 6)

            back_bt= Button(root2, text ="Back",  width = 75,
            command = startpage.flights_av)
            back_bt.grid(row = 7)

        def goa():
            root1.withdraw()
            root2=Tk()
            root2.title("Goa")

            label = Label(root2, text ="Goa", font = LARGEFONT)
            label.grid(row = 1)

            info = Label(root2, text ="Goa is a state in western India with coastlines stretching along the Arabian Sea. Its long history as a Portuguese colony prior to 1961 is evident in its preserved 17th-century churches and the area’s tropical spice plantations", font = TEXT)
            info.grid(row = 2)

            blank = Label(root2, text =" ", font = TEXT)
            blank.grid(row = 3)

            time = Label(root2, text ="AVALIABLE FLIGHT TIME: 2 AM, 3 PM, 8 PM, 11 PM", font = TEXT)
            time.grid(row = 4)

            price = Label(root2, text ="PRICE: 10000 Rs, 6000 Rs, 3800 Rs", font = TEXT)
            price.grid(row = 5)

            button2 = Button(root2, text ="Book a flight",  width = 75,
            command = startpage.airline)
            button2.grid(row = 6)

            back_bt= Button(root2, text ="Back",  width = 75,
            command = startpage.flights_av)
            back_bt.grid(row = 7)


        def melbourne():
            root1.withdraw()
            root2=Tk()
            root2.title("Melbourne")

            label = Label(root2, text ="Melbourne", font = LARGEFONT)
            label.grid(row = 1)

            info = Label(root2, text ="Melbourne is the coastal capital of the southeastern Australian state of Victoria. At the city's centre is the modern Federation Square development, with plazas, bars, and restaurants by the Yarra River. ", font = TEXT)
            info.grid(row = 2)

            blank = Label(root2, text =" ", font = TEXT)
            blank.grid(row = 3)

            time = Label(root2, text ="AVALIABLE FLIGHT TIME: 1 AM, 8 PM", font = TEXT)
            time.grid(row = 4)

            price = Label(root2, text ="PRICE: 10000 Rs, 6000 Rs, 3800 Rs", font = TEXT)
            price.grid(row = 5)

            button2 = Button(root2, text ="Book a flight",  width = 75,
            command = startpage.airline)
            button2.grid(row = 6)

            back_bt= Button(root2, text ="Back",  width = 75,
            command = startpage.flights_av)
            back_bt.grid(row = 7)

        def chennai():
            root1.withdraw()
            root2=Tk()
            root2.title("Chennai")

            label = Label(root2, text ="Chennai", font = LARGEFONT)
            label.grid(row = 1)

            info = Label(root2, text ="Chennai, on the Bay of Bengal in eastern India, is the capital of the state of Tamil Nadu. The city is home to Fort St. George, built in 1644 and now a museum showcasing the city’s roots as a British military garrison and East India Company trading outpost", font = TEXT)
            info.grid(row = 2)

            blank = Label(root2, text =" ", font = TEXT)
            blank.grid(row = 3)

            time = Label(root2, text ="AVALIABLE FLIGHT TIME: 2 AM, 9 AM, 4 PM, 7 PM, 9 PM, 11 PM", font = TEXT)
            time.grid(row = 4)

            price = Label(root2, text ="PRICE: 10000 Rs, 6000 Rs, 3800 Rs", font = TEXT)
            price.grid(row = 5)

            button2 = Button(root2, text ="Book a flight",  width = 75,
            command = startpage.airline)
            button2.grid(row = 6)

            back_bt= Button(root2, text ="Back",  width = 75,
            command = startpage.flights_av)
            back_bt.grid(row = 7)

        def lavasa():
            root1.withdraw()
            root2=Tk()
            root2.title("Lavasa")

            label = Label(root2, text ="Lavasa", font = LARGEFONT)
            label.grid(row = 1)

            info = Label(root2, text ="Lavasa is a private, planned city built near Pune. It is stylistically based on the Italian town Portofino, with a street and several buildings bearing the name of that town.", font = TEXT)
            info.grid(row = 2)

            blank = Label(root2, text =" ", font = TEXT)
            blank.grid(row = 3)

            time = Label(root2, text ="AVALIABLE FLIGHT TIME: 4 PM, 7 PM, 9 PM, 11 PM", font = TEXT)
            time.grid(row = 4)

            price = Label(root2, text ="PRICE: 10000 Rs, 6000 Rs, 3800 Rs", font = TEXT)
            price.grid(row = 5)

            button2 = Button(root2, text ="Book a flight",  width = 75,
            command = startpage.airline)
            button2.grid(row = 6)

            back_bt= Button(root2, text ="Back",  width = 75,
            command = startpage.flights_av)
            back_bt.grid(row = 7)

        button1 = Button(root1, text ="Maldives", width = 75,
        command = maldives)

        button2 = Button(root1, text ="Goa",  width = 75,
        command = goa)

        button3 = Button(root1, text ="Melbourne", width = 75,
        command = melbourne)

        button4= Button(root1, text ="Chennai",  width = 75,
        command = chennai)

        button5= Button(root1, text ="Lavasa",  width = 75,
        command = lavasa)

        button6= Button(root1, text ="Back",  width = 75,
        command = startpage.airline)


        button1.grid(row = 2)
        button2.grid(row = 3)
        button3.grid(row = 4)
        button4.grid(row = 5)
        button5.grid(row = 6)

button1 = Button(fr2,text ="Show flights available", width = 75,
command = startpage.flights_av)

button1.grid(row = 4)

button2 = Button(fr2,text ="Book a flight",  width = 75,
command = startpage.airline)
button2.grid(row = 5)

root.mainloop()
