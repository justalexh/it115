#Imports class library
import tkinter as tk
from tkinter import ttk

#Defines a function that takes an event parameter.
def on_select(event):

    #Creates an item object that obtains the value of the desired item.
    selected_item = event.widget.get()
    print("Selected item", selected_item)


 #Tinkiter GUI app window and setting its title.
root = tk.Tk()
root.title("Alex is cool")   

#Creates an array of items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#Creates a widget for combobox
combo_box = ttk.Combobox(root, values=items)
#Binds the Combobox to the on_select function
combo_box.bind("<<ComboBoxSelected>>", on_select)

combo_box.pack()

#Start the moon event loop for gui application.
root.mainloop()