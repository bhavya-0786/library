import subprocess
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 

# Create main window
window = tkinter.Tk()
window.title("Login form")
window.geometry('320x440+0+100')
window.configure(bg='#333333')

def login():
    username = "bhavya"
    password = "2232"
    if username_entry.get() == username and password_entry.get() == password:
       
       subprocess.call(["python3","2nd.py"])
              
    else:         
        messagebox.showerror(title="Error", message="Invalid login.")

# Create a frame for the content
frame = tkinter.Frame(window)
frame.pack(fill="both", expand=True)

# Load and display the background image
background_image = Image.open("/Users/bhavya/Downloads/ss.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a Label to place the background image
background_label = Label(frame, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FFFFFF", font=("Arial", 45))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="black", font=("Arial", 16), command=login)

# Placing widgets on the screen using place
login_label.place(relx=0.5, rely=0.2, anchor="center")
username_label.place(relx=0.1, rely=0.35, anchor="w")
username_entry.place(relx=0.1, rely=0.4, relwidth=0.8)
password_label.place(relx=0.1, rely=0.5, anchor="w")
password_entry.place(relx=0.1, rely=0.55, relwidth=0.8)
login_button.place(relx=0.5, rely=0.7, anchor="center")

# Start the main loop
window.mainloop()