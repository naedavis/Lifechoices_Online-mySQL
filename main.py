# Naeemah Davis
# Main page
import tkinter#
from tkinter import *
from tkinter import messagebox

from Sign_In_Out import draw_In_Out
from Register import draw_register
from Admin import draw_admin
In_Out = 0

def draw():
    main = Tk()
    main.geometry("800x900")
    main.config(bg="#EBFFEC")
    main.resizable(width=False, height=False)
    main.title("Life Choices Online")

    #### CONTROL + A FUNCTION
    def admin(event):
        main.destroy()
        draw_admin()

    # binding keyboard buttons with main window
    # to allow admin access without logging in
    main.bind("<Control-a>", admin)

    #### ENDS HERE

    #### REGISTER FUNCTION
    def register():
        main.destroy()
        draw_register()

    def signIn():
        In_Out = 1
        main.destroy()
        draw_In_Out(In_Out)

    def signOut():
        main.destroy()
        draw_In_Out(In_Out)

    def exitApplication():
        msg = messagebox.askquestion("EXIT", "Are you sure you want to exit?")
        if msg == "yes":
            main.destroy()
        else:
            pass


    lbl_title = Label(main, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
    lbl_title.place(x=100, y=50)
    btn_Sign_in = Button(main, text="Sign In Here", bg="#71D696", fg="#EBFFEC", font="Arial 30 bold", command=signIn)
    btn_Sign_in.place(x=260, y=350, width=280)
    btn_Sign_out = Button(main, text="Sign Out Here", bg="#71D696", fg="#EBFFEC", font="Arial 30 bold", command=signOut)
    btn_Sign_out.place(x=260, y=450, width=280)
    btn_Register = Button(main, text="Register", bg="#71D696", fg="#EBFFEC", font="Arial 30 bold", command=register)
    btn_Register.place(x=260, y=250, width=280)
    btn_exit = Button(main, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=exitApplication)
    btn_exit.place(x=600, y=700)

    main.mainloop()

if __name__ == '__main__':
#   function where login style and functions are stored is being called to run
    draw()