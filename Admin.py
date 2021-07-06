# Naeemah Davis
# Admin Screen
from tkinter import *
from tkinter import ttk

import mysql.connector as mysql

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
# cursor.execute("SELECT * FROM Sign_In_Out")

def signed_in():
    lbl_title.config(text="")
    lbl_admin.config(text="")
    #### TO SHOW THOSE SIGNED IN
    cursor.execute("SELECT Date,Time,Name FROM Sign_In_Out where Sign_In_Out=1")

    i = 0
    for student in cursor:
        for j in range(len(student)):
            e = Entry(admin, fg='blue', font="Arial 14 bold")
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    #
    # sign_in = cursor.execute("SELECT COUNT(*) FROM Sign_In_Out WHERE Sign_In_Out=1")
    # print(sign_in)
    #### UNTIL HERE






btn_submit = Button(admin, text="Signed-In", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=signed_in)
btn_submit.place(x=550, y=320)
btn_clear = Button(admin, text="Clear", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
btn_clear.place(x=335, y=620, width=120)

btn_back = Button(admin, text="Back", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
btn_back.place(x=60, y=720)


btn_exit = Button(admin, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
btn_exit.place(x=600, y=720, width=120)

admin.mainloop()
