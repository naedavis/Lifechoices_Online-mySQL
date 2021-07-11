# Naeemah Davis
# Main page
# Main page that hold the Register, Sign In and Sign Out buttons
# along with the <CTRL + A> to reach the admin page
from tkinter import *
from tkinter import messagebox

# Importing the functions where the widgets of the windows are stored in
from Sign_In_Out import draw_In_Out
from Register import draw_register
from Admin import draw_admin


# variable declared outside of the main window function
# when the user clicks on Sign In the value of In_Out will change to 1
# when the user clicks on Sign Out it remains the default value of 0
# purpose is so that i didn't have to make two DIFFERENT windows for Sign In and Out
In_Out = 0

#function that holds all widgets and their functions on tkinter window
def draw():
    main = Tk()
    main.geometry("800x900")
    main.config(bg="#EBFFEC")
    main.resizable(width=False, height=False)
    main.title("Life Choices Online")


# ####CONTROL + A FUNCTION ######

    def admin(event):
#       destroys current window
        main.destroy()
#       opens admin window
        draw_admin()

    # binding keyboard buttons with main window
    # to allow admin access without logging in
    main.bind("<Control-a>", admin)

# ###### ENDS HERE  ######

# ---BUTTONS FUNCTIONS---
#   Takes you to the register form
    def register():
        main.destroy()
        draw_register()
#   takes you to the sign in form
    def signIn():
#       changing in out value, so table knows that the user is signed in
        In_Out = 1
        main.destroy()
#       imports Sign In window with the In_Out value being sent to that screen so the table knows the user is signing in
        draw_In_Out(In_Out)
#   takes you to the sign out window
    def signOut():
        main.destroy()
#       imports sign out window with the In_Out Default value so the table know the user is signing out
        draw_In_Out(In_Out)
#   quits the screen
    def exitApplication():
#   asks if the user is sure they want to exit
        msg = messagebox.askquestion("EXIT", "Are you sure you want to exit?")
        if msg == "yes":
            main.destroy()
        else:
            pass

# ---END OF BUTTON FUNCTIONS---

#   ---LABEL AND BUTTON WIDGETS (THAT ARE CALLING THEIR FUNCTIONS DECLARED ABOVE)---
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
#   ---END OF LABEL AND BUTTON WIDGETS---
    main.mainloop()

if __name__ == '__main__':
#   function where login style and functions are stored is being called to run
    draw()