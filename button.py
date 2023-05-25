#Imports tinkter library.
import tkinter as tk


#Create & Define a function for when button is clickd.
def button_click():
        print("Buton clicked!")


#Parent or root window.
root = tk.Tk() 
root.title("Button Example")       

#Creates a button with the class library, text ,function call.
button =tk.Button(root,text="Click Me!", command=button_click)
button.pack()

#Creates a mainloop to keep the root window open.
root.mainloop()