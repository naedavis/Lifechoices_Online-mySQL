# Naeemah Davis
# Main page
import tkinter#
from tkinter import *

main = Tk()
main.geometry("800x900")
main.config(bg="#EBFFEC")
main.resizable(width=False, height=False)
main.title("Life Choices Online")

lbl_title = Label(main, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
lbl_title.place(x=100,y=50)
btn_Sign_in = Button(main, text="Sign In Here", bg="#71D696", fg="#EBFFEC", font="Arial 30 bold")
btn_Sign_in.place(x=260, y=350, width=280)
btn_Sign_out = Button(main, text="Sign Out Here", bg="#71D696", fg="#EBFFEC", font="Arial 30 bold")
btn_Sign_out.place(x=260, y=450, width=280)
btn_Register = Button(main, text="Register", bg="#71D696", fg="#EBFFEC", font="Arial 30 bold")
btn_Register.place(x=260, y=250, width=280)
btn_exit = Button(main, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold")
btn_exit.place(x=600, y=700)


main.mainloop()