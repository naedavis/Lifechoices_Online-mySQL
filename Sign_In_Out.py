# Naeemah Davis
# Sign in and Out form
from tkinter import *

# from main import draw
from tkinter import messagebox

import mysql.connector as mysql


def draw_In_Out(In_Out):
    sign = Tk()
    sign.geometry("800x800")
    sign.config(bg="#EBFFEC")
    sign.resizable(width=False, height=False)
    sign.title("Life Choices Online")
    print(In_Out)

    lbl_title = Label(sign, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
    lbl_title.place(x=110, y=20)
    lbl_sign = Label(sign, text="Sign In/Out", fg="#71D696", bg="#EBFFEC", font="Purisa 30 bold")
    lbl_sign.place(x=250, y=130)

    # FUNCTIONS

    def sign_in():
        if e_name.get() == "" or e_idNo.get() == "":
            messagebox.showerror("Error", "Please Fill in all fields")
        else:
            try:
                db = mysql.connect(host="localhost", user="lifechoices",
                                   password="@Lifechoices1234", database="Lifechoices_Online")
                cursor = db.cursor()
                cursor.execute(
                    "Select * from Registration where Name='" + e_name.get() + "' and ID_No='" + e_idNo.get() + "'")
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Name or ID")
                    e_name.delete(0, END)
                    e_idNo.delete(0, END)
                    e_name.focus_set()
                else:
                    cursor.execute("Insert into SignInOutTable values(curdate(), '"+e_idNo.get()+"', '"+e_name.get()+"','"+str(In_Out)+"',curtime(),null);")
                    db.commit()
                    db.close()
                    messagebox.showinfo("Successful Sign In", "Welcome " + e_name.get())
                    sign.destroy()

            except ValueError as x:
                messagebox.showerror("Error", "Enter Valid Details")

    def sign_out():
        if e_name.get() == "" or e_idNo.get() == "":
            messagebox.showerror("Error", "Please Fill in all fields")
        else:
            try:
                db = mysql.connect(host="localhost", user="lifechoices",
                                   password="@Lifechoices1234", database="Lifechoices_Online")
                cursor = db.cursor()
                cursor.execute(
                    "Select * from Registration where Name='" + e_name.get() + "' and ID_No='" + e_idNo.get() + "'")
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Name or ID")
                    e_name.delete(0, END)
                    e_idNo.delete(0, END)
                    e_name.focus_set()
                else:
                    cursor.execute(
                        "Insert into SignInOutTable values(curdate(), '" + e_idNo.get() + "', '" + e_name.get() + "','" + str(
                            In_Out) + "',curtime(),null);")
                    db.commit()
                    db.close()
                    messagebox.showinfo("Successful Sign Out", "Good Bye, " + e_name.get())
                    sign.destroy()




            except ValueError as x:
                messagebox.showerror("Error", "Enter Valid Details")

    lbl_name = Label(sign, text="Name:", fg="#206F3D", bg="#EBFFEC", font="Poppins 22")
    lbl_name.place(x=250, y=300)
    e_name = Entry(sign, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_name.place(x=250, y=340)
    lbl_idNo = Label(sign, text="ID No:", fg="#206F3D", bg="#EBFFEC", font="Poppins 22")
    lbl_idNo.place(x=250, y=400)
    e_idNo = Entry(sign, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
    e_idNo.place(x=250, y=440)

    btn_signIn = Button(sign, text="Sign In", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_in)
    btn_signIn.place(x=250, y=520)
    btn_signOut = Button(sign, text="Sign Out", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_out)
    btn_signOut.place(x=400, y=520)

    if In_Out == 1:
        btn_signOut.config(state="disabled")
    else:
        btn_signIn.config(state="disabled")

    btn_clear = Button(sign, text="Clear", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
    btn_clear.place(x=335, y=620, width=120)

    btn_back = Button(sign, text="Back", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
    btn_back.place(x=60, y=720)

    btn_exit = Button(sign, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
    btn_exit.place(x=600, y=720, width=120)

    sign.mainloop()


if __name__ == '__main__':
    draw_In_Out("")
