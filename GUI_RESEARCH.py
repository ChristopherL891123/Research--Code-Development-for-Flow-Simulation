#https://edube.org/learn/pcpp1-4-gui-programming/settling-widgets-in-the-window-s-interior-3

import tkinter
from tkinter import messagebox #used to display message boxes to the user # https://realpython.com/lessons/import-statement/
def showMessage1():
    messagebox.showinfo("  ","    ")

def EXITmyGUI():#this is used to tell the program what to do when it is clicked
    QuitMessage = messagebox.askyesno("Quit?","Are you sure you want to quit the application?") #returns Boolean value
    if QuitMessage == True: #if the user wants to quit
        myGUI.destroy()# closes the window

myGUI = tkinter.Tk() #starts the GUI, invisible until the event controller starts
myGUI.title("Numerical Simulation of Arterial Blood Flow") # must be called before the main controller or it won't show the title


label1 = tkinter.Label(myGUI,text= "The purpose of this research is to model a numerical flow simulation of the one-dimensional Poiseuille model using Python code. ")
label1.grid(row=0,column=1)
label2 = tkinter.Label(myGUI,text= "I intend to use LU decomposition and then implement forward and backward elimination to solve for velocity.")
label2.grid(row=1,column=1)


AButton = tkinter.Button(myGUI,text="Button", command= showMessage1)
AButton.grid(row=2,column=1)
ExitButton = tkinter.Button(myGUI,text="EXIT",height=1,width=10,background="light blue", foreground='black',command= EXITmyGUI) # in command= , it does not accept the function name and the parenthesis, only the function name
                            #text is what text the button will hold, background is the color of the utton and foreground is the color of the text of the button

ExitButton.grid(row=5,column=1)
myGUI.mainloop()

