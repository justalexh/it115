#Imports class library
import tkinter as tk
from tkinter import ttk

#Defines a function that takes an event parameter.
def on_select(event):

    #Creates an item object that obtains the value of the desired item.
    selected_item = event.widget.get()
    print("Selected item"), selected_item)


 #Tinkiter GUI app window and setting its title.
root = tk.Tk()
root.title("Alex is cool")   

#
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#
combo_box = ttk.Combobox(root, values=items)