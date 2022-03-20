#https://edube.org/learn/pcpp1-4-gui-programming/settling-widgets-in-the-window-s-interior-3

import tkinter
from tkinter import messagebox #used to display message boxes to the user
import main

def GUI():
    def showMessage():
        messagebox.showinfo("Generating", "Generating results")  # note: \n can  be used

    def showError():
        messagebox.showerror("Error","ERROR: Size of matrix A must be a positive integer.")

    def EXITmyGUI():  # this is used to tell the program what to do when it is clicked
        QuitMessage = messagebox.askyesno("Quit?","Are you sure you want to quit the application?")  # returns Boolean value
        if QuitMessage == True:
            myGUI.destroy()

    def display():
        try:
            if int(Textbox.get("1.0","end")) >= 0:
                messagebox.showinfo("","GENERATING")
                main.main_GUI(int(Textbox.get("1.0","end")))

                labelTable.delete(1.0,"end")
                labelTable.insert(1.0,main.GUI_table)

        except:
            messagebox.showinfo("", "ERROR: Size of matrix A must be a positive integer.")
            import traceback
            traceback.print_exc()

    myGUI = tkinter.Tk()
    myGUI.geometry("1500x800")
    myGUI.title("Code Development for Flow Simulation")

    label1 = tkinter.Label(myGUI,text= "The purpose of this research is to model a numerical flow simulation of the one-dimensional Poiseuille model using Python code. ",font=("Times", "12"))
    label1.place(x=100,y=0)
    label2 = tkinter.Label(myGUI,text= "I intend to use LU decomposition and then implement forward and backward elimination to solve for velocity at the discrete points.",font=("Times", "12"))
    label2.place(x=100,y=20)

    label3 = tkinter.Label(myGUI,text="Size of matrix A to generate: ",font=("Times", "12","bold"))
    label3.place(x=300,y=60)

    SubmitButton = tkinter.Button(myGUI,text="Submit", command= display)
    SubmitButton.place(x=600,y=60)

    Textbox = tkinter.Text(myGUI,height=2,width=10)
    Textbox.place(x=500,y=60)

    scrollbar = tkinter.Scrollbar(myGUI)
    scrollbar.place(x=300,y=90)
    labelTable = tkinter.Text(myGUI,height=40,width=150)
    labelTable.place(x=100,y=100)

    ExitButton = tkinter.Button(myGUI,text="EXIT",height=1,width=10,background="light blue", foreground='black',command= EXITmyGUI)

    ExitButton.place(x=500,y=750)
    myGUI.mainloop()


GUI()
