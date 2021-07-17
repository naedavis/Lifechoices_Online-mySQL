# Naeemah Davis
# Sign in and Out form
from tkinter import *

from tkinter import messagebox
# import unittest
import mysql.connector as mysql

#   ---FUNCTION THAT HOLDS ALL THE WIDGETS AND FUNCTION OF THE SIGN IN AND OUT WINDOW---
def draw_In_Out(In_Out):
    sign = Tk()
    sign.geometry("800x800")
    sign.config(bg="#EBFFEC")
    sign.resizable(width=False, height=False)
    sign.title("Life Choices Online")

#   ---HEADING LABELS---
    lbl_title = Label(sign, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
    lbl_title.place(x=110, y=20)
    lbl_sign = Label(sign, text="Sign In/Out", fg="#71D696", bg="#EBFFEC", font="Purisa 30 bold")
    lbl_sign.place(x=250, y=130)
#   ---END OF HEADING LABELS

# ---FUNCTIONS ---

#   ---SIGN IN FUNCTION---
    def sign_in():
#       Validation, if name or id entries are empty, show error message
        if e_name.get() == "" or e_idNo.get() == "":
            messagebox.showerror("Error", "Please Fill in all fields")
        else:
            try:
#               when the data meets the requirements, the databse is opened and we are now able to write queries inside
                db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4426099",
                   password="uzgsckcuvd", database="sql4426099", port="3306")
                cursor = db.cursor()
#               query written to show all the information in the Register table
                cursor.execute(
                    "Select * from Register where Name='" + e_name.get() + "' and ID_No='" + e_idNo.get() + "'")
#               fetches data in the table to see if the user actually exists and is registered
                row = cursor.fetchone()
                if row is None:
#                   if the user does not exist or ID is incorrect show error message
                    messagebox.showerror("Error", "Invalid Name or ID")
                    e_name.delete(0, END)
                    e_idNo.delete(0, END)
                    e_name.focus_set()
                else:
#                   HOWEVER if the information given is correct, query below will insert the name and ID No
#                   along with the In_Out value, which is signed in and current time and date of signing in
                    cursor.execute("Insert into SignInOutTable values(curdate(), '"+e_idNo.get()+"', '"+e_name.get()+"','"+str(In_Out)+"',curtime(),null);")
                    db.commit()
                    db.close()
                    messagebox.showinfo("Successful Sign In", "Welcome " + e_name.get())
                    sign.destroy()

            except ValueError as x:
                messagebox.showerror("Error", "Enter Valid Details")
#   ---END OF SIGN IN FUNCTION---

#   ---SIGN OUT FUNCTION---
    def sign_out():
#       Validation, if name or id entries are empty, show error message
        if e_name.get() == "" or e_idNo.get() == "":
            messagebox.showerror("Error", "Please Fill in all fields")
        else:
            try:
#               when the data meets the requirements, the databse is opened and we are now able to write queries inside
                db = mysql.connect(host="sql4.freesqldatabase.com", user="sql4426099",
                           password="uzgsckcuvd", database="sql4426099", port="3306")
                cursor = db.cursor()
#               query written to show all the information in the Register table
                cursor.execute(
                    "Select * from Register where Name='" + e_name.get() + "' and ID_No='" + e_idNo.get() + "'")
                row = cursor.fetchone()
#               fetches data in the table to see if the user actually exists and is registered
                if row == None:
#                   if the user does not exist or ID is incorrect show error message
                    messagebox.showerror("Error", "Invalid Name or ID")
                    e_name.delete(0, END)
                    e_idNo.delete(0, END)
                    e_name.focus_set()
                else:
 #                   HOWEVER if the information given is correct, query below will insert the name and ID No
#                   along with the In_Out value, which is signed out and current time and date of signing out
                    cursor.execute(
                        "Insert into SignInOutTable values(curdate(), '" + e_idNo.get() + "', '" + e_name.get() + "','" + str(
                            In_Out) + "',curtime(),null);")
                    db.commit()
                    db.close()
                    messagebox.showinfo("Successful Sign Out", "Good Bye, " + e_name.get())
                    sign.destroy()
            except ValueError as x:
                messagebox.showerror("Error", "Enter Valid Details")
#   ---END OF SIGNING OUT FUNCTION---

#   ---CLEAR FUNCTION---
    def clear():
        e_name.delete(0,END)
        e_idNo.delete(0,END)
#   ---END OF CLEAR FUNCTION---

#   ---EXIT APPLICATION FUNCTION---
    def exit_application():
        msg = messagebox.askquestion("EXIT", "Are you sure you want to exit?")
        if msg == "yes":
            sign.destroy()
        else:
            pass

#   ---LABEL WIDGETS---
    lbl_name = Label(sign, text="Name:", fg="#206F3D", bg="#EBFFEC", font="Poppins 22")
    lbl_name.place(x=250, y=300)
    e_name = Entry(sign, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_name.place(x=250, y=340)
    lbl_idNo = Label(sign, text="ID No:", fg="#206F3D", bg="#EBFFEC", font="Poppins 22")
    lbl_idNo.place(x=250, y=400)
    e_idNo = Entry(sign, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_idNo.place(x=250, y=440)
#   ---END OF LABEL WIDGETS---

#   ---BUTTON WIDGETS WHERE ABOVE FUNCTIONS ARE CALLED TO ACTION---
    btn_signIn = Button(sign, text="Sign In", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_in)
    btn_signIn.place(x=250, y=520)
    btn_signOut = Button(sign, text="Sign Out", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_out)
    btn_signOut.place(x=400, y=520)
#   ---END OF BUTTONS---

#   --- SOME EXTRA PARAMETERS SO THAT WHEN THE USER CLICKS SIGNING IN, THEY ARE ONLY ABLE TO SIGN IN AND VICE VERSA---
#   IF the In_Out value is 1, thats means the user clicked on Sign-In so DISABLE THE SIGN OUT BUTTON TO AVOID CONFUSION
    if In_Out == 1:
        btn_signOut.config(state="disabled")
    else:
#   IF the In_Out value is 0, thats means the user clicked on Sign-Out so DISABLE THE SIGN OUT BUTTON TO AVOID CONFUSION
        btn_signIn.config(state="disabled")

    btn_clear = Button(sign, text="Clear", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=clear)
    btn_clear.place(x=335, y=620, width=120)

    btn_exit = Button(sign, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold",command=exit_application)
    btn_exit.place(x=600, y=720, width=120)

    sign.mainloop()


if __name__ == '__main__':
    draw_In_Out("")
