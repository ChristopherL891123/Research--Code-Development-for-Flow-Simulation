import tkinter
from tkinter import messagebox #used to display message boxes to the user
def EXITmyGUI():#this is used to tell the program what to do when it is clicked
    QuitMessage = messagebox.askyesno("Quit?","Are you sure you want to quit the application?") #returns Boolean value
    if QuitMessage == True: #if the user wants to quit
        myGUI.destroy()# closes the window

myGUI = tkinter.Tk() #starts the GUI, invisible until the event controller starts
myGUI.title("Numerical Simulation of Arterial Blood Flow") # must be called before the main controller or it won't show the title
ExitButton = tkinter.Button(myGUI,text="EXIT",height=5,width=25,background="light blue", command= EXITmyGUI) #created, but not placed! in command= , it does not accept the function name and the parenthesis, only the function name
ExitButton.place(x=700,y=500)





myGUI.mainloop()

