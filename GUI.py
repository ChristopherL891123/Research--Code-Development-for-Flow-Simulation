# https://edube.org/learn/pcpp1-4-gui-programming/settling-widgets-in-the-window-s-interior-3

import tkinter
from tkinter import messagebox  # used to display message boxes to the user
import main
import matplotlib.pyplot as plt
import LU
import MatrixGeneration as m


def EXITmyGUI():  # this is used to tell the program what to do when it is clicked
    QuitMessage = messagebox.askyesno("Quit?",
                                      "Are you sure you want to quit the application?")  # returns Boolean value
    if QuitMessage == True:
        myGUI.destroy()


def clearTextbox():
    labelTable.delete(1.0, "end")


def display():
    try:
        c = 0.0  #
        t = int(Textbox.get("1.0", "end").strip())
        if t > 0:
            A = m.GENERATE(t)
            GUI_table, x, y_points = LU.SOLVE(A, t, GUI=True)

            pltTitle = "Graph for {i} discrete points".format(i=t + 2)
            # labelTable.delete(1.0, "end")  #

            labelTable.insert(1.0, "{a} \n\n\n".format(a=pltTitle))
            labelTable.insert(c, GUI_table)  #
            c += 1.0
            plt.plot(x, y_points)
            plt.title(pltTitle)
            plt.show()

    except:
        messagebox.showinfo("", "ERROR: Size of matrix A must be a positive integer.")
        import traceback
        traceback.print_exc()


myGUI = tkinter.Tk()
myGUI.geometry("1500x800")
myGUI.title("Code Development for Flow Simulation")

label1 = tkinter.Label(myGUI, text="The purpose of this research is to model a "
                                   "numerical flow simulation of the one-dimensional Poiseuille model using Python "
                                   "code. ", font=("Times", "12"))
label1.place(x=100, y=0)
label2 = tkinter.Label(myGUI, text="I intend to use LU decomposition and then implement forward and backward "
                                   "elimination to solve for velocity at the discrete points.", font=("Times", "12"))
label2.place(x=100, y=20)

label3 = tkinter.Label(myGUI, text="Size of matrix A to generate: ", font=("Times", "12", "bold"))
label3.place(x=300, y=60)

SubmitButton = tkinter.Button(myGUI, text="Submit", command=display)
SubmitButton.place(x=600, y=60)

Textbox = tkinter.Text(myGUI, height=2, width=10)
Textbox.place(x=500, y=60)

labelTable = tkinter.Text(myGUI, height=40, width=150)
labelTable.place(x=100, y=100)

clearButton = tkinter.Button(myGUI, text="CLEAR", command=clearTextbox)
clearButton.place(x=1350, y=250)

ExitButton = tkinter.Button(myGUI, text="EXIT", height=1, width=10, background="light blue", foreground='black',
                            command=EXITmyGUI)
ExitButton.place(x=500, y=750)

myGUI.mainloop()
