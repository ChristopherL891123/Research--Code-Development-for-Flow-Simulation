# Christopher Lama

import tkinter
from tkinter import messagebox  # used to display message boxes to the user
import matplotlib.pyplot as plt
import LU
import MatrixGeneration as m

# concepts learned from https://edube.org/study/pcpp1-3

def EXITmyGUI():
    """
    Description:
        Generates a pop-up window that confirms if the user would like to exit the program. This is generated when the user clicks the blue button at
        the bottom of the screen.

    Parameters:
        none

    Returns:
        None
        """

    QuitMessage = messagebox.askyesno("Quit?", "Are you sure you want to quit the application?")  # returns Boolean value
    if QuitMessage == True:
        myGUI.destroy() #close the window

def clearTextbox():
    """
    Description:
        Clears the textbox where the tables are printed out.

    Parameters:
        None

    Returns:
        None
            """
    labelTable.delete(1.0, "end")

def display():
    """
    Description:
        Asks for inputs from the user and solves the matrix equation using those values.
        Displays a graph of results and table of calculations.

    Parameters:
        None

    Returns:
        None
    """
    try:
        #get values from the textboxes
        n = int(Textbox.get("1.0", "end").strip())
        length = float(textboxL.get("1.0", "end").strip())
        nu = float(textboxNu.get("1.0", "end").strip())
        DeltaP = float(textboxDeltaP.get("1.0", "end").strip())
        h = float(textboxH.get("1.0", "end").strip())

        # generate the A matrix and solve the system of linear equations
        A = m.GENERATE(n)
        GUI_table, x, y_points = LU.SOLVE(A, n, True,l=length,deltaP=DeltaP,Nu=nu,H=h)

        # insert description of the table
        labelTable.insert(1.0, "Table for "+str(n+2)+" discrete points, η = "+str(nu)+ ", Length of channel = "+str(length)+", Radius = "+str(h)+", ΔP = "+str(DeltaP)+'\n')

        # insert table
        labelTable.insert(2.0, GUI_table + '\n\n')  #https://www.pythontutorial.net/tkinter/tkinter-text/
        # 2.0 is LineNumber.ColumnNumber

        # set up the graph
        plt.margins(x=0,y=0)
        plt.plot(x, y_points)
        plt.title("Graph for {i} discrete points".format(i=n + 2))
        plt.xlabel("Velocity", fontsize=12)
        plt.ylabel("y",rotation="horizontal",fontsize=12)
        plt.show()

    except:
        import traceback
        messagebox.showinfo("Error", "ERROR: ERROR: values provided caused an error")
        traceback.print_exc() # shows the cause of the error

# create and place window and window elements
myGUI = tkinter.Tk() # create Tkinter object
myGUI.geometry("1500x800") # create window of 1500x800 pixels
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
SubmitButton.place(x=478, y=155)

Textbox = tkinter.Text(myGUI, height=2, width=10)
Textbox.place(x=500, y=60)

labelNu = tkinter.Label(myGUI,text='η: ',font=("Times", "12", "bold") )
labelNu.place(x=140,y=110)

textboxNu = tkinter.Text(myGUI, height=2, width=10)
textboxNu.place(x=160,y=110)

labelL = tkinter.Label(myGUI,text="Length of channel: ", font=("Times", "12", "bold") )
labelL.place(x=250,y=110)
textboxL = tkinter.Text(myGUI, height=2, width=10)
textboxL.place(x=380,y=110)

labelDeltaP = tkinter.Label(myGUI,text="ΔP: ",font=("Times", "12", "bold"))
labelDeltaP.place(x=480,y=110)
textboxDeltaP = tkinter.Text(myGUI, height=2, width=10)
textboxDeltaP.place(x=530,y=110)

labelH = tkinter.Label(myGUI,text="Radius H: ", font=("Times", "12", "bold") )
labelH.place(x=630,y=110)
textboxH = tkinter.Text(myGUI, height=2, width=10)
textboxH.place(x=710,y=110)

labelTable = tkinter.Text(myGUI, height=35, width=180)
labelTable.place(x=10, y=185)

clearButton = tkinter.Button(myGUI, text="CLEAR", command=clearTextbox)
clearButton.place(x=1455, y=250)

ExitButton = tkinter.Button(myGUI, text="EXIT", height=1, width=10, background="light blue",
                            foreground='black', command=EXITmyGUI)
ExitButton.place(x=500, y=750)

myGUI.mainloop() # keeps the program running until the window is closed.