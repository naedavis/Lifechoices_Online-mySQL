# Naeemah Davis
# Register Screen
from tkinter import *
from tkinter import messagebox
import unittest
import mysql.connector as mysql

# importing from Sign In/ Out window, so after registering, the user has the option to sign in
from Sign_In_Out import draw_In_Out


#   ---Function that holds the Widgets of Register window---
def draw_register():
    register = Tk()
    register.geometry("800x900")
    register.config(bg="#EBFFEC")
    register.resizable(width=False, height=False)
    register.title("Life Choices Online")
#   ---Heading Labels---
    lbl_title = Label(register, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
    lbl_title.place(x=110, y=20)
    lbl_register = Label(register, text="Registration", fg="#71D696", bg="#EBFFEC", font="Purisa 30 bold")
    lbl_register.place(x=250, y=100)
    lbl_details = Label(register, text="Personal Details", fg="#206F3D", bg="#EBFFEC", font="Poppins 20")
    lbl_details.place(x=250, y=190)
#   ---End of Heading Labels---

#   ---LABEL AND ENTRY WIDGETS NEEDED FOR REGISTRATION---
    lbl_name = Label(register, text="Name:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_name.place(x=250, y=240)
    e_name = Entry(register, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_name.place(x=250, y=270)
    lbl_surname = Label(register, text="Surname:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_surname.place(x=250, y=320)
    e_surname = Entry(register, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_surname.place(x=250, y=350)
    lbl_idno = Label(register, text="ID Number:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_idno.place(x=250, y=400)
    e_id = Entry(register, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_id.place(x=250, y=430)
    lbl_contactno = Label(register, text="Contact No:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_contactno.place(x=250, y=480)
    e_contact = Entry(register, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_contact.place(x=250, y=510)
    lbl_nextok = Label(register, text="Next of Kin Details", fg="#206F3D", bg="#EBFFEC", font="Poppins 20")
    lbl_nextok.place(x=250, y=570)
    lbl_nextokname = Label(register, text="Name:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_nextokname.place(x=250, y=620)
    e_nextok_name = Entry(register, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_nextok_name.place(x=250, y=650)
    lbl_nextok_contactno = Label(register, text="Contact No:", fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    lbl_nextok_contactno.place(x=250, y=700)
    e_nextok_contactno = Entry(register, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_nextok_contactno.place(x=250, y=730)
#   ---END OF LABELS AND ENTRY WIDGETS---


# ---FUNCTIONS---

#   ---REGISTER FUNCTION--
    def register_now():
#       Validation to make sure the entries are not empty when inserting them into the table
        if e_name.get() == "" or e_id.get() == "" or e_contact.get() == "" or e_surname.get() == "" or e_nextok_name.get() == "" or e_nextok_contactno.get() == "":
#           if they are empty, show this message
            messagebox.showerror("Error!", "Please fill in ALL fields")
        else:
            try:
#               Validation to check the length of the ID Number and Contact Numbers
                if len(e_id.get()) != 13 or len(e_contact.get()) != 10 or len(e_nextok_contactno.get()) != 10:
                    print("Invalid Data Type")
                else:
#                   when data meets requirements, it opens up the database
                    db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4426099",
                           password="uzgsckcuvd", database="sql4426099", port="3306")
                    cursor = db.cursor()
#                   declaring a variable that fetches each item of data in the database
                    row = cursor.fetchone()
#                   if the data it fetched matches any user already registered, an error message will be showed and all entries cleared
                    if row is not None:
                        messagebox.showerror("Error", "This user already exists")
                        e_name.delete(0, END)
                        e_surname.delete(0, END)
                        e_id.delete(0, END)
                        e_contact.delete(0, END)
                        e_nextok_name.delete(0, END)
                        e_nextok_contactno.delete(0, END)
                    else:
#                       HOWEVER if the user doesnt exist, do the following:
#                       Database query to insert the data into the Register Table
                        cursor.execute(
                            "INSERT into Register values(null,'" + e_name.get() + "','" + e_surname.get() + "','" + e_id.get() + "','" + e_contact.get() + "','" + e_nextok_name.get() + "','" + e_nextok_contactno.get() + "');")
#                       after inserting, .commit basically updates your table with the information received
                        db.commit()
#                       make sure to close the db to prevent any data being messed with
                        db.close()
#                       message to sya registration was successful AND to aks if the user would like to sign in
                        msg = messagebox.askquestion("REGISTRATION SUCCESSFUL",
                                                     "You are now Registered on Lifechoices Online \n Would you like to Sign In?")
                        if msg == "Yes":
                            register.destroy()
#                           if the user decides to sign in, In_Out variable is now 1 to indicate Sign In
                            draw_In_Out(In_Out=1)
                        else:
                            register.destroy()
            except ValueError as x:
                messagebox.showerror("ERROR", "Enter Valid Entries")
#   ---END OF REGISTER FUNCTION---

# ---CLEAR FUNCTION---
    def clear():
        e_name.delete(0, END)
        e_surname.delete(0, END)
        e_id.delete(0, END)
        e_contact.delete(0, END)
        e_nextok_name.delete(0, END)
        e_nextok_contactno.delete(0, END)
#       after clearing the entries, put the cursor in the first entry for user convenience
        e_name.focus_set()
#   ---END OF CLEAR FUNCTION

#   ---EXIT FUNCTION---
    def exitApplication():
        msg = messagebox.askquestion("EXIT", "Are you sure you want to exit?")
        if msg == "yes":
            register.destroy()
        else:
            e_name.delete(0, END)
            e_surname.delete(0, END)
            e_id.delete(0, END)
            e_contact.delete(0, END)
            e_nextok_name.delete(0, END)
            e_nextok_contactno.delete(0, END)
#   ---END OF EXIT APPLICATION

#   ---BUTTONS WHERE ABOVE FUNCTIONS WILL BE CALLED (SO WHEN THEY'RE PRESSED, THE FUNCTION WILL EXECUTE)---
    btn_submit = Button(register, text="SUBMIT", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=register_now)
    btn_submit.place(x=300, y=820)
    btn_clear = Button(register, text="Clear", bg="grey", fg="#EBFFEC", font="Arial 25 bold",command=clear)
    btn_clear.place(x=600, y=720, width=120)
    btn_exit = Button(register, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=exitApplication)
    btn_exit.place(x=600, y=820, width=120)
#   ---END OF BUTTONS WITH FUNCTIONS---

    register.mainloop()

    # class test_register(unittest.TestCase):
    #     def test_id(self):
    #       draw_register(register_now(len(e_id.get())=[13]))
if __name__ == '__main__':
    draw_register()
