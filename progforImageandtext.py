from tkinter import * 
  
# creating tkinter window 
root = Tk() 
  
# Adding widgets to the root window 
Label(root, text = 'Multispectral_Laboratory', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
  
# Creating a photoimage object to use image 
photo = PhotoImage(file = r"D:/M.Tech3rdSem/WorkProject/GUIWork/sir.jpg") 
  
# here, image option is used to 
# set image on button 
Button(root, text = 'Click Me !', image = photo).pack(side = TOP) 
  
mainloop() 
