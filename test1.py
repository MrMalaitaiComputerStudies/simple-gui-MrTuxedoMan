# Author: 
# Date: 
# The purpose of this is to demonstrate the ability to create a simple GUI, commit, and then push it so that Mr Malaitai can read it.

# The GUI is to have the following:
# 1 Label widget that says "Enter name"
# 1 Entry widget next to the Label widget
# 1 Button widget that spans over 2 columns underneath the Label and Entry widgets.
import tkinter as tk

root = tk.Tk()

l1 = tk.Label(root, text = "Enter name")
l1.grid(row = 0, column = 0)
e1 = tk.Label(root)
e1.grid(row = 0, column = 1)
b1 = tk.Button(root, text = "Button")
b1.grid(row = 1, column = 0, columnspan = 2)

root.mainloop()
