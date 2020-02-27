from tkinter import *
import DataFrame

master = Tk()
 
def callback():
    DataFrame.Read_Bands()
    DataFrame.Plot_Bands()
    print ("click!")
 
b = Button(master, text="Click", command=callback)
b.pack()
 
mainloop()
