# Naeemah Davis
# Admin Screen
import datetime
from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector as mysql
from tkcalendar import Calendar



def draw_admin():
    admin = Tk()
    admin.geometry("800x800")
    admin.config(bg="#EBFFEC")
    admin.resizable(width=False, height=False)
    admin.title("Life Choices Online")

    lbl_title = Label(admin, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
    lbl_title.place(x=100, y=20)
    lbl_admin = Label(admin, text="Admin", fg="#71D696", bg="#EBFFEC", font="Purisa 30 bold")
    lbl_admin.place(x=280, y=130)

    db = mysql.connect(host="localhost", user="lifechoices",
                       password="@Lifechoices1234", database="Lifechoices_Online")
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
    lbl_detailsOf = Label(admin, text="Showing Details of:", fg="#206F3D", bg="#EBFFEC", font="Arial 15 bold")
    lbl_detailsOf.place(x=50, y=480)

    def search():
        def back_search():
            admin.destroy()
            import main

        lbl_title.config(text="")
        lbl_admin.config(text="")
        ### TO CHECK ALL THAT HAS SIGNED IN
        cursor.execute("select "
                       " Date,ID_No, Name, In_Out, Time"
                       " from SignInOutTable where Date='" + cal.get_date() + "' and Name='" + stvar.get() + "'")

        tree = ttk.Treeview(admin)
        tree['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

        # assigning properties of columns
        tree.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree.column("Name", width=120, minwidth=120, anchor=CENTER)
        # tree.column("ID No", width=200)
        tree.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree.column("Time", width=50, minwidth=50, anchor=CENTER)

        # heading names
        tree.heading("Date", text="Date")
        tree.heading("ID_No", text="ID_No")
        tree.heading("Name", text="Name")
        # tree.heading("ID No", text="ID No")
        tree.heading("Sign In/Out", text="Sign In/Out")
        tree.heading("Time", text="Time")

        # For loop
        # allows for the records in "SignInOutTable"
        # to be displayed in the treeview diagram in correct order
        i = 0
        for user in cursor:
            tree.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4]))
            i = +1

        tree.place(x=50, y=70, width=650, height=150)

    def sign_in():
        lbl_title.config(text="")
        lbl_admin.config(text="")
        ### TO CHECK ALL THAT HAS SIGNED IN
        cursor.execute("select "
                       " max(Date) Date,max(ID_No) ID_No, Name,"
                       " if(In_Out = 1, 'Signed In', 'Signed Out') Sign_In_Out, max(Time) Time"
                       " from SignInOutTable where In_Out = 1 and Date=curdate() and Time>Time"
                       " group by Date, Name ")

        tree = ttk.Treeview(admin)
        tree['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

        # assigning properties of columns
        tree.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree.column("Name", width=120, minwidth=120, anchor=CENTER)
        # tree.column("ID No", width=200)
        tree.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree.column("Time", width=50, minwidth=50, anchor=CENTER)

        # heading names
        tree.heading("Date", text="Date")
        tree.heading("ID_No", text="ID_No")
        tree.heading("Name", text="Name")
        # tree.heading("ID No", text="ID No")
        tree.heading("Sign In/Out", text="Sign In/Out")
        tree.heading("Time", text="Time")

        # For loop
        # allows for the records in "SignInOutTable"
        # to be displayed in the treeview diagram in correct order
        i = 0
        for user in cursor:
            tree.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4]))
            i = +1

        tree.place(x=50, y=70, width=650, height=150)
        ### ENDS HERE

    def sign_out():
        lbl_title.config(text="")
        lbl_admin.config(text="")
        ### TO CHECK ALL THAT HAS SIGNED OUT
        cursor.execute("select "
                       " max(Date) Date,max(ID_No) ID_No, max(Name) Name,"
                       " if(In_Out = 1, 'Signed In', 'Signed Out') Sign_In_Out, max(Time) Time"
                       " from SignInOutTable where In_Out = 0 and Date=curdate()"
                       "group by Time")

        tree = ttk.Treeview(admin)
        tree['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

        # assigning properties of columns
        tree.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree.column("Name", width=120, minwidth=120, anchor=CENTER)
        # tree.column("ID No", width=200)
        tree.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree.column("Time", width=50, minwidth=50, anchor=CENTER)

        # heading names
        tree.heading("Date", text="Date")
        tree.heading("ID_No", text="ID_No")
        tree.heading("Name", text="Name")
        # tree.heading("ID No", text="ID No")
        tree.heading("Sign In/Out", text="Sign In/Out")
        tree.heading("Time", text="Time")

        # For loop
        # allows for the records in "SignInOutTable"
        # to be displayed in the treeview diagram in correct order
        i = 0
        for user in cursor:
            tree.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4]))
            i = +1

        tree.place(x=50, y=70, width=650, height=150)
        ### ENDS HERE

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

    query = cursor.execute("Select name from SignInOutTable group by name having count(*)>1")
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

    btn_signIn = Button(admin, text="Signed-In", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_in)
    btn_signIn.place(x=570, y=430, width=200)
    btn_signOut = Button(admin, text="Signed-Out", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_out)
    btn_signOut.place(x=570, y=500, width=200)
    btn_search = Button(admin, text="Search", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=search)
    btn_search.place(x=570, y=300, width=200)

    cursor.execute("Select Count(*) from SignInOutTable where Date=curdate() and Time<=curtime() and In_Out=1;")
    test_g = PhotoImage(file="green.png")
    img_g = Label(bg="white", border="0", image=test_g)
    img_g.image = test_g
    img_g.place(x=50, y=640, width=50, height=50)
    lbl_g = Button(admin, highlightthickness=0, text="15", fg="white", bd="0", font="Arial 20 bold", bg="#a8d484")
    lbl_g.place(x=60, y=650, width=30, height=30)
    lbl_active = Label(admin, text="Users Signed In", fg="#206F3D", bg="#EBFFEC", font="Arial 20 bold")
    lbl_active.place(x=110, y=650)

    btn_insert = Button(admin, text="Insert", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=exitApplication)
    btn_insert.place(x=570, y=720, width=200)
    btn_exit = Button(admin, text="Delete", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=exitApplication)
    btn_exit.place(x=570, y=720, width=200)
    for n in cursor:
        lbl_g.config(text=n)

    btn_exit = Button(admin, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold",command=exitApplication)
    btn_exit.place(x=570, y=720, width=200)

    admin.mainloop()

if __name__ == '__main__':
    draw_admin()