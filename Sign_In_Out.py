# Naeemah Davis
# Sign in and Out form
from tkinter import *

sign = Tk()
sign.geometry("800x800")
sign.config(bg="#EBFFEC")
sign.resizable(width=False, height=False)
sign.title("Life Choices Online")

lbl_title = Label(sign, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
lbl_title.place(x=110,y=20)
lbl_sign = Label(sign, text="Sign In/Out", fg="#71D696", bg="#EBFFEC", font="Purisa 30 bold")
lbl_sign.place(x=250, y=130)

lbl_name = Label(sign, text="Name:", fg="#206F3D", bg="#EBFFEC", font="Poppins 22")
lbl_name.place(x=250, y=300)
e_name = Entry(sign, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
e_name.place(x=250, y=340)
lbl_idNo = Label(sign, text="ID No:",fg="#206F3D", bg="#EBFFEC", font="Poppins 22")
lbl_idNo.place(x=250, y=400)
e_idNo = Entry(sign, fg="#206F3D", bg="#EBFFEC", font="Poppins 18")
e_idNo.place(x=250, y=440)

btn_submit = Button(sign, text="SUBMIT", fg="#206F3D", bg="#71D696", font="Arial 25 bold")
btn_submit.place(x=320, y=520)
btn_clear = Button(sign, text="Clear", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
btn_clear.place(x=335, y=620, width=120)

btn_back = Button(sign, text="Back", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
btn_back.place(x=60, y=720)


btn_exit = Button(sign, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
btn_exit.place(x=600, y=720, width=120)

sign.mainloop()
