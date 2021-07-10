# Naeemah Davis
# Admin Screen
import datetime
from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector as mysql
from tkcalendar import Calendar

from Register_admin import draw_admin_register


def draw_admin():
    admin = Tk()
    admin.geometry("800x900")
    admin.config(bg="#EBFFEC")
    admin.resizable(width=False, height=False)
    admin.title("Life Choices Online")

    lbl_title = Label(admin, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
    lbl_title.place(x=100, y=20)
    lbl_admin = Label(admin, text="Admin", fg="#71D696", bg="#EBFFEC", font="Purisa 30 bold")
    lbl_admin.place(x=280, y=130)


    db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4424128",
                       password="8aQSEf2XsR", database="sql4424128", port="3306")
    cursor = db.cursor()

    # Calender to choose a date from
    # Making variables to hold current year, month and date to allow flexibility in calendar
    x = datetime.datetime.now()
    year = x.year
    month = x.month
    day = x.day

    cal = Calendar(admin, selectmode='day',
                   year=year, month=month,
                   day=day)
    cal.place(x=50, y=250, width=250, height=200)


    def search():

        lbl_title.config(text="")
        lbl_admin.config(text="")
        ### TO CHECK ALL THAT HAS SIGNED IN
        cursor.execute("select "
                       " Date,ID_No, Name, In_Out, Time"
                       " from SignInOutTable where Date='" + cal.get_date() + "' and Name='" + stvar.get() + "'")

        tree_search = ttk.Treeview(admin)
        tree_search['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree_search["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

        # assigning properties of columns
        tree_search.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree_search.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree_search.column("Name", width=120, minwidth=120, anchor=CENTER)
        tree_search.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree_search.column("Time", width=50, minwidth=50, anchor=CENTER)

        # heading names
        tree_search.heading("Date", text="Date")
        tree_search.heading("ID_No", text="ID_No")
        tree_search.heading("Name", text="Name")
        tree_search.heading("Sign In/Out", text="Sign In/Out")
        tree_search.heading("Time", text="Time")

        # For loop
        # allows for the records in "SignInOutTable"
        # to be displayed in the treeview diagram in correct order
        i = 0
        for user in cursor:
            tree_search.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4]))
            i = +1

        tree_search.place(x=50, y=70, width=650, height=150)

    def sign_in():
        lbl_title.config(text="")
        lbl_admin.config(text="")
        ### TO CHECK ALL THAT HAS SIGNED IN
        cursor.execute("select "
                       " max(Date) Date,max(ID_No) ID_No, Name,"
                       " if(In_Out = 1, 'Signed In', 'Signed Out') Sign_In_Out, max(Time) Time"
                       " from SignInOutTable where In_Out = 1 and Date=curdate()"
                       " group by Date, Name;")

        tree_in = ttk.Treeview(admin)
        tree_in['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree_in["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

        # assigning properties of columns
        tree_in.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree_in.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree_in.column("Name", width=120, minwidth=120, anchor=CENTER)
        tree_in.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree_in.column("Time", width=50, minwidth=50, anchor=CENTER)

        # heading names
        tree_in.heading("Date", text="Date")
        tree_in.heading("ID_No", text="ID_No")
        tree_in.heading("Name", text="Name")
        tree_in.heading("Sign In/Out", text="Sign In/Out")
        tree_in.heading("Time", text="Time")

        # For loop
        # allows for the records in "SignInOutTable"
        # to be displayed in the treeview diagram in correct order
        for user in cursor:
            tree_in.insert('', user[6], text="", values=(user[0], user[1], user[2], user[3], user[4], user[5]))

        tree_in.place(x=50, y=70, width=700, height=150)
        ### ENDS HERE

    def sign_out():
        lbl_title.config(text="")
        lbl_admin.config(text="")
        ### TO CHECK ALL THAT HAS SIGNED OUT
        cursor.execute("select "
                       " max(Date) Date,max(ID_No) ID_No, max(Name) Name,"
                       " if(In_Out = 1, 'Signed In', 'Signed Out') Sign_In_Out, max(Time) Time"
                       " from SignInOutTable where In_Out = 0 and Date=curdate()"
                       "group by Time;")

        tree_out = ttk.Treeview(admin)
        tree_out['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree_out["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

        # assigning properties of columns
        tree_out.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree_out.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree_out.column("Name", width=120, minwidth=120, anchor=CENTER)
        tree_out.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree_out.column("Time", width=50, minwidth=50, anchor=CENTER)

        # heading names
        tree_out.heading("Date", text="Date")
        tree_out.heading("ID_No", text="ID_No")
        tree_out.heading("Name", text="Name")
        tree_out.heading("Sign In/Out", text="Sign In/Out")
        tree_out.heading("Time", text="Time")

        # For loop
        # allows for the records in "SignInOutTable"
        # to be displayed in the treeview diagram in correct order
        i = 0
        for user in cursor:
            tree_out.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4]))
            i = +1

        tree_out.place(x=50, y=70, width=700, height=150)
        ### ENDS HERE
    def register():
        lbl_title.config(text="")
        lbl_admin.config(text="")
        btn_search.destroy()
        db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4424128",
                           password="8aQSEf2XsR", database="sql4424128", port="3306")
        cursor = db.cursor()
        cursor.execute("Select Name, Surname, ID_No, Contact, NextOfKinName, NextOfKinContact , id from Register")
        tree_insert = ttk.Treeview(admin)
        tree_insert['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree_insert["columns"] = ( "Name", "Surname", "ID No", "Contact No","NextOfKin Name", "NextOfKin Contact")

        # assigning properties of columns
        tree_insert.column("Name", width=50, minwidth=50, anchor=CENTER)
        tree_insert.column("Surname", width=50, minwidth=50, anchor=CENTER)
        tree_insert.column("ID No", width=100, minwidth=100, anchor=CENTER)
        tree_insert.column("Contact No", width=100, minwidth=100, anchor=CENTER)
        tree_insert.column("NextOfKin Name", width=50, minwidth=50, anchor=CENTER)
        tree_insert.column("NextOfKin Contact", width=100, minwidth=100, anchor=CENTER)

        # heading names
        tree_insert.heading("Name", text="Name")
        tree_insert.heading("Surname", text="Surname")
        tree_insert.heading("ID No", text="ID No")
        tree_insert.heading("Contact No", text="Contact No")
        tree_insert.heading("NextOfKin Name", text="NextOfKin Name")
        tree_insert.heading("NextOfKin Contact", text="NextOfKin Contact")

        # For loop
        # allows for the records in "SignInOutTable"
        # to be displayed in the treeview diagram in correct order
        for user in cursor:
            tree_insert.insert('', user[6], text="", values=(user[0], user[1], user[2], user[3], user[4],user[5]))


        v_scroll = ttk.Scrollbar(tree_insert, orient="vertical")
        v_scroll.configure(command=tree_insert.yview)
        tree_insert.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(fill=Y, side=RIGHT)

        tree_insert.place(x=50, y=70, width=700, height=150)
    def edit():
        admin.destroy()
        draw_admin_register()


    def exitApplication():
        msg = messagebox.askquestion("EXIT", "Are you sure you want to exit?")
        if msg == "yes":
            admin.destroy()
        else:
            pass

    ######################
    my_list = []
    stvar = StringVar(admin)
    stvar.set(['Choose Name'])

    cursor.execute("Select name from Register group by name having count(*)")
    i = 0
    for user in cursor:
        my_list.append(user[0])
        i = +1
    print(my_list)
    menu = OptionMenu(admin, stvar, *my_list, command=None)
    menu.config(fg="#71D696", bg="#EBFFEC", font="Arial 18 bold")
    menu["menu"].config(fg="#71D696", bg="#EBFFEC", font="Arial 15")
    menu.place(x=330, y=305, width=230)
    name_of_person = stvar.get()
    ######################
    btn_register = Button(admin, text="Register", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=register)
    btn_register.place(x=570, y=360, width=200)
    btn_signIn = Button(admin, text="Signed-In", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_in)
    btn_signIn.place(x=570, y=430, width=200)
    btn_signOut = Button(admin, text="Signed-Out", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_out)
    btn_signOut.place(x=570, y=500, width=200)
    btn_search = Button(admin, text="Search", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=search)
    btn_search.place(x=570, y=300, width=200)
    btn_edit = Button(admin, text="Edit", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=edit)
    btn_edit.place(x=570, y=560, width=200)


    cursor.execute("Select Count(*) from SignInOutTable where Date=curdate() and In_Out=1;")
    test_g = PhotoImage(file="green.png")
    img_g = Label(bg="white", border="0", image=test_g)
    img_g.image = test_g
    img_g.place(x=50, y=640, width=50, height=50)
    lbl_g = Button(admin, highlightthickness=0, text="", fg="white", bd="0", font="Arial 20 bold", bg="#a8d484")
    lbl_g.place(x=60, y=650, width=30, height=30)
    lbl_active = Label(admin, text="Users Signed In", fg="#206F3D", bg="#EBFFEC", font="Arial 20 bold")
    lbl_active.place(x=110, y=650)


    for n in cursor:
        lbl_g.config(text=n)


    btn_exit = Button(admin, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=exitApplication)
    btn_exit.place(x=570, y=720, width=200)

    admin.mainloop()


if __name__ == '__main__':
    draw_admin()
