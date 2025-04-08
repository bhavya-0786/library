import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()

# Set the size of the window
root.geometry("320x440+670+100")

# Set the background color to 'PeachPuff'
root.configure(bg="PeachPuff")

# Title of the window (optional)
root.title("Availability Of Book")


# Add a label in the middle for "Book Name"
label_middle = tk.Label(root, text="Book Name", bg="PeachPuff",fg="IndianRed", font=("Arial", 20))
label_middle.place(x=100, y=140)

# Add an entry box below the "Book Name" label
combo_box = ttk.Combobox(root, font=("Arial", 12), values=["Book 1", "Book 2", "Book 3"])
combo_box.place(x=80, y=170)

# Function to update the selected book label
def check_book():
    selected_book.set(f"Selected Book: {combo_box.get()}")

# Add a button below the entry box
button = tk.Button(root, text="Check", font=("Arial", 12), bg="IndianRed", fg="Black", command=check_book)
button.place(x=120, y=210)

# Add a decorative design using Canvas below the buttons
canvas = tk.Canvas(root, width=340, height=50, bg="PeachPuff", highlightthickness=0)
canvas.pack()

# Draw a simple design on the canvas (a line and some shapes)
canvas.create_line(0, 50, 320, 50, fill="IndianRed", width=3)
canvas.create_oval(130, 30, 190, 90, outline="IndianRed", width=2)

# Add a label at the bottom to show the selected book
selected_book = tk.StringVar()
selected_book.set("Selected Book : None")
selected_book_label = tk.Label(root, textvariable=selected_book, bg="PeachPuff",fg="IndianRed", font=("Arial", 14))
selected_book_label.place(x=85,y=360)

# Add a label at the bottom to show the availability
avail_book = tk.StringVar()
avail_book.set("Availability : None")
avail_book_label = tk.Label(root, textvariable=avail_book, bg="PeachPuff",fg="IndianRed", font=("Arial", 14))
avail_book_label.place(x=95,y=390)


# Start the Tkinter loop
root.mainloop()
