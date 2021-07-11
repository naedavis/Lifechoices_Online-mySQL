# Naeemah Davis
# Admin Screen
# Press Ctrl + a to get to this page
import datetime
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as mysql
from tkcalendar import Calendar

from Register_admin import draw_admin_register

#   ---FUNCTION THAT HOLDS ALL THE WIDGETS AND FUNCTION OF THE ADMIN WINDOW---
def draw_admin():
    admin = Tk()
    admin.geometry("800x900")
    admin.config(bg="#EBFFEC")
    admin.resizable(width=False, height=False)
    admin.title("Life Choices Online")
#   ---HEADING LABELS---
    lbl_title = Label(admin, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
    lbl_title.place(x=100, y=20)
    lbl_admin = Label(admin, text="Admin", fg="#71D696", bg="#EBFFEC", font="Purisa 30 bold")
    lbl_admin.place(x=280, y=130)
#   ---END OF HEADING LABELS---

#   ---CONNECTING THE DATABASE HOSTED DATABASE FOR USE---
    db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4424128",
                       password="8aQSEf2XsR", database="sql4424128", port="3306")
    cursor = db.cursor()

#   ---CALENDAR---
#   ---VARIABLES THAT HOLD TODAY'S DATE TO BE INSERTED IN THE CALENDAR AS THE DEFAULT DATE---
    x = datetime.datetime.now()
    year = x.year
    month = x.month
    day = x.day

    cal = Calendar(admin, selectmode='day',
                   year=year, month=month,
                   day=day)
    cal.place(x=50, y=250, width=250, height=200)
#   ---END OF CALENDAR---

#   ---SEARCH FUCNTION---
    def search():
#       REMOVING THE HEADINGS TO MAKE SPACE FOR TREEVIEW
        lbl_title.config(text="")
        lbl_admin.config(text="")
#       QUERY TO DISPLAY * THE RECORDS IN THE SIGN IN AND OUT TABLE OF A SPECIFIC PERSON ON SPECIFIC DATE
        cursor.execute("select "
                       " Date,ID_No, Name, In_Out, Time"
                       " from SignInOutTable where Date='" + cal.get_date() + "' and Name='" + stvar.get() + "'")
#       ---TREEVIEW INITIATION---
#       USED TO DISPLAY THE TABLES IN THE DATABASE
        tree_search = ttk.Treeview(admin)
#       NEED TO SPECIFY THAT ONLY COLUMNS WITH HEADINGS SHOULD SHOW, OTHERWISE THERE'S AN EMPTY FIRST COLUMN
        tree_search['show'] = "headings"
#       DEFINING THE NUMBER OF COULMNS TO STORE THE TABLES DATA
        tree_search["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

#       ASSIGNING PROPERTIES TO THE TABLE
        tree_search.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree_search.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree_search.column("Name", width=120, minwidth=120, anchor=CENTER)
        tree_search.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree_search.column("Time", width=50, minwidth=50, anchor=CENTER)

#       HEADING NAMES OF TABLE
        tree_search.heading("Date", text="Date")
        tree_search.heading("ID_No", text="ID_No")
        tree_search.heading("Name", text="Name")
        tree_search.heading("Sign In/Out", text="Sign In/Out")
        tree_search.heading("Time", text="Time")

#       ---FOR LOOP---
#       ALLOWS FOR RECORDS TO BE TAKEN FROM THE DATABASE TABLE AND INSERTED IN THE TREEVIEW TABLE,  IN THE CORRECT ORDER
        i = 0
        for user in cursor:
            tree_search.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4]))
            i = +1

        tree_search.place(x=50, y=70, width=650, height=150)
#       ---END OF TREEVIEW---

#   ---SIGN IN FUNCTION---
    def sign_in():
# REMOVING THE HEADINGS TO MAKE SPACE FOR TREEVIEW
        lbl_title.config(text="")
        lbl_admin.config(text="")
#       QUERY TO DISPLAY * THE RECORDS IN THE SIGN IN AND OUT TABLE OF THOSE WHO ARE SIGNED IN
        cursor.execute("select "
                       " max(Date) Date,max(ID_No) ID_No, Name,"
                       " if(In_Out = 1, 'Signed In', 'Signed Out') Sign_In_Out, max(Time) Time"
                       " from SignInOutTable where In_Out = 1 and Date=curdate()"
                       " group by Date, Name;")
#       ---TREEVIEW INITIATION---
#       USED TO DISPLAY THE TABLES IN THE DATABASE
        tree_in = ttk.Treeview(admin)
#       NEED TO SPECIFY THAT ONLY COLUMNS WITH HEADINGS SHOULD SHOW, OTHERWISE THERE'S AN EMPTY FIRST COLUMN
        tree_in['show'] = "headings"
#       DEFINING THE NUMBER OF COLUMNS TO STORE THE TABLES DATA
        tree_in["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

#       ASSIGNING PROPERTIES TO THE TABLE
        tree_in.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree_in.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree_in.column("Name", width=120, minwidth=120, anchor=CENTER)
        tree_in.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree_in.column("Time", width=50, minwidth=50, anchor=CENTER)

#       HEADING NAMES OF TABLE
        tree_in.heading("Date", text="Date")
        tree_in.heading("ID_No", text="ID_No")
        tree_in.heading("Name", text="Name")
        tree_in.heading("Sign In/Out", text="Sign In/Out")
        tree_in.heading("Time", text="Time")

#       ---FOR LOOP---
#       ALLOWS FOR RECORDS TO BE TAKEN FROM THE DATABASE TABLE AND INSERTED IN THE TREEVIEW TABLE,  IN THE CORRECT ORDER
        for user in cursor:
            tree_in.insert('', user[6], text="", values=(user[0], user[1], user[2], user[3], user[4], user[5]))

        tree_in.place(x=50, y=70, width=700, height=150)
#       ---END OF TREEVIEW---
#   ---END OF SIGN IN FUNCTION---

#   ---SIGN OUT FUNCTION---
    def sign_out():
#       REMOVING THE HEADINGS TO MAKE SPACE FOR TREEVIEW
        lbl_title.config(text="")
        lbl_admin.config(text="")
#       QUERY TO DISPLAY * THE RECORDS IN THE SIGN IN AND OUT TABLE OF THOSE WHO ARE SIGNED OUT
        cursor.execute("select "
                       " max(Date) Date,max(ID_No) ID_No, max(Name) Name,"
                       " if(In_Out = 1, 'Signed In', 'Signed Out') Sign_In_Out, max(Time) Time"
                       " from SignInOutTable where In_Out = 0 and Date=curdate()"
                       "group by Time;")
#       ---TREEVIEW INITIATION---
#       USED TO DISPLAY THE TABLES IN THE DATABASE
        tree_out = ttk.Treeview(admin)
#       NEED TO SPECIFY THAT ONLY COLUMNS WITH HEADINGS SHOULD SHOW, OTHERWISE THERE'S AN EMPTY FIRST COLUMN
        tree_out['show'] = "headings"
#       DEFINING THE NUMBER OF COLUMNS TO STORE THE TABLES DATA
        tree_out["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")

#       ASSIGNING PROPERTIES TO THE TABLE
        tree_out.column("Date", width=100, minwidth=100, anchor=CENTER)
        tree_out.column("ID_No", width=120, minwidth=120, anchor=CENTER)
        tree_out.column("Name", width=120, minwidth=120, anchor=CENTER)
        tree_out.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
        tree_out.column("Time", width=50, minwidth=50, anchor=CENTER)

#       HEADING NAMES OF TABLE
        tree_out.heading("Date", text="Date")
        tree_out.heading("ID_No", text="ID_No")
        tree_out.heading("Name", text="Name")
        tree_out.heading("Sign In/Out", text="Sign In/Out")
        tree_out.heading("Time", text="Time")

#       ---FOR LOOP---
#       ALLOWS FOR RECORDS TO BE TAKEN FROM THE DATABASE TABLE AND INSERTED IN THE TREEVIEW TABLE,  IN THE CORRECT ORDER
        i = 0
        for user in cursor:
            tree_out.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4]))
            i = +1

        tree_out.place(x=50, y=70, width=700, height=150)
#       ---END OF TREEVIEW---
#   ---END OF SIGN IN FUNCTION---

#   ---REGISTER FUNCTION---
#   SHOWS THE ABLE OF THOSE WHO ARE REGISTERED
    def register():
#       REMOVING THE HEADINGS TO MAKE SPACE FOR TREEVIEW
        lbl_title.config(text="")
        lbl_admin.config(text="")
        btn_search.destroy()
#   ---CONNECTING THE DATABASE HOSTED DATABASE FOR USE---
        db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4424128",
                           password="8aQSEf2XsR", database="sql4424128", port="3306")
        cursor = db.cursor()
#       QUERY TO DISPLAY * THE RECORDS IN THE REGISTER TABLE
        cursor.execute("Select Name, Surname, ID_No, Contact, NextOfKinName, NextOfKinContact , id from Register")
#       ---TREEVIEW INITIATION---
#       USED TO DISPLAY THE TABLES IN THE DATABASE
        tree_insert = ttk.Treeview(admin)
#       NEED TO SPECIFY THAT ONLY COLUMNS WITH HEADINGS SHOULD SHOW, OTHERWISE THERE'S AN EMPTY FIRST COLUMN
        tree_insert['show'] = "headings"
#       DEFINING THE NUMBER OF COLUMNS TO STORE THE TABLES DATA
        tree_insert["columns"] = ( "Name", "Surname", "ID No", "Contact No","NextOfKin Name", "NextOfKin Contact")

#       ASSIGNING PROPERTIES TO THE TABLE
        tree_insert.column("Name", width=50, minwidth=50, anchor=CENTER)
        tree_insert.column("Surname", width=50, minwidth=50, anchor=CENTER)
        tree_insert.column("ID No", width=100, minwidth=100, anchor=CENTER)
        tree_insert.column("Contact No", width=100, minwidth=100, anchor=CENTER)
        tree_insert.column("NextOfKin Name", width=50, minwidth=50, anchor=CENTER)
        tree_insert.column("NextOfKin Contact", width=100, minwidth=100, anchor=CENTER)

#       HEADING NAMES OF TABLE
        tree_insert.heading("Name", text="Name")
        tree_insert.heading("Surname", text="Surname")
        tree_insert.heading("ID No", text="ID No")
        tree_insert.heading("Contact No", text="Contact No")
        tree_insert.heading("NextOfKin Name", text="NextOfKin Name")
        tree_insert.heading("NextOfKin Contact", text="NextOfKin Contact")

#       ---FOR LOOP---
#       ALLOWS FOR RECORDS TO BE TAKEN FROM THE DATABASE TABLE AND INSERTED IN THE TREEVIEW TABLE,  IN THE CORRECT ORDER
        for user in cursor:
            tree_insert.insert('', user[6], text="", values=(user[0], user[1], user[2], user[3], user[4],user[5]))
#       VERTICAL SCROOLBAR INITIATED IN CASE THE REGISTER HAS TOO MANY REGISTERED
        v_scroll = ttk.Scrollbar(tree_insert, orient="vertical")
        v_scroll.configure(command=tree_insert.yview)
        tree_insert.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(fill=Y, side=RIGHT)
#       END OF VERTICAL SCROLLBAR

        tree_insert.place(x=50, y=70, width=700, height=150)
#       ---END OF TREEVIEW---
#   ---END OF REGISTER FUNCTION---

#   ---EDIT FUNCTION---
#   TAKES USER TO REGISTER ADMIN WINDOW TO BE A BLE TO DELETE AND INSERT AND UPDATE REGISTER TABLE
    def edit():
        admin.destroy()
        draw_admin_register()
#   ---END OF EDIT FUNCTION---

#   ---EXIT APPLICATION FUNCTION---
    def exitApplication():
        msg = messagebox.askquestion("EXIT", "Are you sure you want to exit?")
        if msg == "yes":
            admin.destroy()
        else:
            pass
#   ---END OF EXIT APPLICATION FUCNTION---

#   ---OPTION MENU---
#   EMPTY LIST TO STORE OPTIONS
    my_list = []
#   DECLARING STRING VARIABLE TYPE THAT WILL HOLD THE NAMES TO CHOOSE FROM
    stvar = StringVar(admin)
# DEFAULT VALUE OF STRING VARIABLE
    stvar.set(['Choose Name'])
#   QUERY THAT SELECTS ALL THE NAMES IN THE REGISTER FORM SO THEY CAN BE VALUES IN THE OPTION MENU
    cursor.execute("Select name from Register group by name having count(*)")
#   ---LOOP---
#   "NAME" COLUMN RECORDS WILL BE ADDED TO THE EMPTY LIST DECLARED ABOVE
#
    i = 0
    for user in cursor:
        my_list.append(user[0])
        i = +1

    menu = OptionMenu(admin, stvar, *my_list, command=None)
    menu.config(fg="#71D696", bg="#EBFFEC", font="Arial 18 bold")
    menu["menu"].config(fg="#71D696", bg="#EBFFEC", font="Arial 15")
    menu.place(x=330, y=305, width=230)
    name_of_person = stvar.get()
#   ---END OF OPTION MENU---

#   ---BUTTON WIDGETS THAT CALL THE FUNCTIONS DECLARED ABOVE---
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
    btn_exit = Button(admin, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=exitApplication)
    btn_exit.place(x=570, y=720, width=200)
#   ---END OF BUTTON WIDGETS---

#   QUERY THAT COUNTS THE AMOUNT OF PEOPLE SIGNED IN
    cursor.execute("Select Count(*) from SignInOutTable where Date=curdate() and In_Out=1;")
#   IMAGE AND BUTTON WIDGETS USED TO DISPLAY THE AMOUNT RECEIVED FROM THE ABOVE QUERY
    test_g = PhotoImage(file="green.png")
    img_g = Label(bg="white", border="0", image=test_g)
    img_g.image = test_g
    img_g.place(x=50, y=640, width=50, height=50)
    lbl_g = Button(admin, highlightthickness=0, text="", fg="white", bd="0", font="Arial 20 bold", bg="#a8d484")
    lbl_g.place(x=60, y=650, width=30, height=30)
#   LABEL WIDGET
    lbl_active = Label(admin, text="Users Signed In", fg="#206F3D", bg="#EBFFEC", font="Arial 20 bold")
    lbl_active.place(x=110, y=650)

#   ---FOR LOOP---
#   TAKING THE VALUE AND INSERTING IT IN THE BUTTON DECLARED ABOVE'S TEXT VALUE
    for n in cursor:
        lbl_g.config(text=n)

    admin.mainloop()

if __name__ == '__main__':
    draw_admin()
