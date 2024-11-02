# Introduction to tkinter in Python

# Import the tkinter module
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("My First GUI")

# Set the size of the window
root.geometry("400x400")

# Create a label widget
label = tk.Label(root, text="Hello, World!")

# Pack the label widget
label.pack()

# Run the main loop
root.mainloop()
