# Naeemah davis
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector as mysql


def draw_admin_register():

    reg_admin = Tk()
    reg_admin.geometry("800x900")
    reg_admin.config(bg="#EBFFEC")
    reg_admin.resizable(width=False, height=False)
    reg_admin.title("Life Choices Online")

    db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4424128",
                       password="8aQSEf2XsR", database="sql4424128", port="3306")
    cursor = db.cursor()
    cursor.execute("Select Name, Surname, ID_No, Contact, NextOfKinName, NextOfKinContact from Register")
    tree_insert = ttk.Treeview(reg_admin)
    tree_insert['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
    # define number of columns
    tree_insert["columns"] = ( "Name", "Surname", "ID No", "Contact No", "NextOfKin Name", "NextOfKin Contact")

    # assigning properties of columns

    tree_insert.column("Name", width=50, minwidth=50, anchor=CENTER)
    tree_insert.column("Surname", width=50, minwidth=50, anchor=CENTER)
    tree_insert.column("ID No", width=100, minwidth=100, anchor=CENTER)
    tree_insert.column("Contact No", width=100, minwidth=100, anchor=CENTER)
    tree_insert.column("NextOfKin Name", width=50, minwidth=50, anchor=CENTER)
    tree_insert.column("NextOfKin Contact", width=100, minwidth=100, anchor=CENTER)

    # heading names
    # tree_insert.heading("id", text="id")
    tree_insert.heading("Name", text="Name")
    tree_insert.heading("Surname", text="Surname")
    tree_insert.heading("ID No", text="ID No")
    tree_insert.heading("Contact No", text="Contact No")
    tree_insert.heading("NextOfKin Name", text="NextOfKin Name")
    tree_insert.heading("NextOfKin Contact", text="NextOfKin Contact")

    # For loop
    # allows for the records in "SignInOutTable"
    # to be displayed in the treeview diagram in correct order
    i = 0
    for user in cursor:
        tree_insert.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4], user[5]))
        i = +1

    v_scroll = ttk.Scrollbar(tree_insert, orient="vertical")
    v_scroll.configure(command=tree_insert.yview)
    tree_insert.configure(yscrollcommand=v_scroll.set)
    v_scroll.pack(fill=Y, side=RIGHT)

    tree_insert.place(x=50, y=70, width=700, height=150)

    lbl_name = Label(reg_admin, text="Name:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_name.place(x=250, y=240)
    e_name = Entry(reg_admin, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_name.place(x=250, y=270)
    lbl_surname = Label(reg_admin, text="Surname:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_surname.place(x=250, y=320)
    e_surname = Entry(reg_admin, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_surname.place(x=250, y=350)
    lbl_idno = Label(reg_admin, text="ID Number:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_idno.place(x=250, y=400)
    e_id = Entry(reg_admin, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_id.place(x=250, y=430)
    lbl_contactno = Label(reg_admin, text="Contact No:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_contactno.place(x=250, y=480)
    e_contact = Entry(reg_admin, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_contact.place(x=250, y=510)
    lbl_nextok = Label(reg_admin, text="Next of Kin Details", fg="#206F3D", bg="#EBFFEC", font="Poppins 20")
    lbl_nextok.place(x=250, y=570)
    lbl_nextokname = Label(reg_admin, text="Name:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_nextokname.place(x=250, y=620)
    e_nextok_name = Entry(reg_admin, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_nextok_name.place(x=250, y=650)
    lbl_nextok_contactno = Label(reg_admin, text="Contact No:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_nextok_contactno.place(x=250, y=700)
    e_nextok_contactno = Entry(reg_admin, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_nextok_contactno.place(x=250, y=730)

##### FUNCTIONS

    def update():
        db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4424128",
                           password="8aQSEf2XsR", database="sql4424128", port="3306")
        cursor = db.cursor()
        cursor.execute("Select Name, Surname, ID_No, Contact, NextOfKinName, NextOfKinContact from Register")
        tree_insert = ttk.Treeview(reg_admin)
        tree_insert['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree_insert["columns"] = ("Name", "Surname", "ID No", "Contact No", "NextOfKin Name", "NextOfKin Contact")

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
        i = 0
        for user in cursor:
            tree_insert.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4], user[5]))
            i = +1

        v_scroll = ttk.Scrollbar(tree_insert, orient="vertical")
        v_scroll.configure(command=tree_insert.yview)
        tree_insert.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(fill=Y, side=RIGHT)
        tree_insert.place(x=50, y=70, width=700, height=150)

    def insert():
        if e_name.get() == "" or e_id.get() == "" or e_contact.get() == "" or e_surname.get() == "" or e_nextok_name.get() == "" or e_nextok_contactno.get() == "":
            messagebox.showerror("Error!", "Please fill in ALL fields")
        else:
            try:
                if len(e_id.get()) != 13 or len(e_contact.get()) != 10 or len(e_nextok_contactno.get()) != 10:
                    print("Invalid Data Type")
                else:
                    db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4424128",
                                       password="8aQSEf2XsR", database="sql4424128", port="3306")
                    cursor = db.cursor()
                    row = cursor.fetchone()
                    if row is not None:
                        messagebox.showerror("Error", "This user already exists")
                        e_name.delete(0, END)
                        e_surname.delete(0, END)
                        e_id.delete(0, END)
                        e_contact.delete(0, END)
                        e_nextok_name.delete(0, END)
                        e_nextok_contactno.delete(0, END)
                    else:
                        cursor.execute(
                            "INSERT into Register values(null,'" + e_name.get() + "','" + e_surname.get() + "','" + e_id.get() + "','" + e_contact.get() + "','" + e_nextok_name.get() + "','" + e_nextok_contactno.get() + "');")
                        db.commit()
                        db.close()
                        messagebox.askquestion("REGISTRATION SUCCESSFUL",
                                        e_name.get() + " is now Registered on Lifechoices Online")

            except ValueError as x:
                messagebox.showerror("ERROR", "Enter Valid Entries")

    def delete():
        if e_name.get() == "" or e_id.get() == "":
            messagebox.showerror("Error", "Please fill in BOTH Name and ID fields when deleting")
        else:
            try:
                db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4424128",
                                   password="8aQSEf2XsR", database="sql4424128", port="3306")
                cursor = db.cursor()
                cursor.execute(
                    "Select * from Register")
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Name or ID")
                    e_name.delete(0, END)
                    e_id.delete(0, END)
                    e_name.focus_set()
                else:
                    cursor.execute(
                        "delete from Register where ID_No='"+e_id.get()+"' and Name='"+e_name.get()+"'")
                    db.commit()
                    db.close()
                    messagebox.showinfo("Successful Deletion",  e_name.get() + ", has been deleted from the Register table " )
            except ValueError as x:
                pass


    btn_update = Button(reg_admin, text="Update", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=update)
    btn_update.place(x=570, y=720, width=200)
    btn_insert = Button(reg_admin, text="Insert", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=insert)
    btn_insert.place(x=570, y=580, width=200)
    btn_delete = Button(reg_admin, text="Delete", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=delete)
    btn_delete.place(x=570, y=650, width=200)

    reg_admin.mainloop()
if __name__ == '__main__':
    #   function where login style and functions are stored is being called to run
    draw_admin_register()