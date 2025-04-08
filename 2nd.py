import tkinter as tk
import subprocess


# Create the main window
root = tk.Tk()
root.title("Library System")
root.geometry("340x440+325+100") 
root.configure(bg="PeachPuff")  #

# Function to show a message when a button is clicked and simulate button press effect
def on_button_click(button, message):
    # Change the button to appear clicked (sunken relief)
    button.config(relief="sunken", state="disabled")
    
    # Update the label with the message
    response_label.config(text=message)
    
    # After 200ms, return the button to its normal state (raised relief)
    root.after(200, lambda: button.config(relief="raised", state="normal"))

# Functions to call different Python scripts
def mem_form():
    subprocess.call(["python3", "3rd.py"])

def issue_return():
    subprocess.call(["python3", "4th.py"])

def avail_but():
    subprocess.call(["python3", "5th.py"])

# Create a label with the text "Welcome to Library" with Indian Red color
label = tk.Label(root, text="Welcome To The Library", font=("Helvetica", 25), 
                 pady=20, bg="PeachPuff", fg="IndianRed")
label.pack()

# Create buttons for "Issue Book", "Return Book", and "Check Availability"
mf_button = tk.Button(root, text="Membership Form", width=20, height=2, 
                      bg="PeachPuff", fg="IndianRed", command=mem_form)
mf_button.pack(pady=10)

ir_button = tk.Button(root, text="Issue/Return Book", width=20, height=2, 
                      bg="PeachPuff", fg="IndianRed", command=issue_return)
ir_button.pack(pady=10)

availability_button = tk.Button(root, text="Check Availability", width=20, height=2, 
                                bg="PeachPuff", fg="IndianRed", command=avail_but)
availability_button.pack(pady=10)

# Create a label to display the message below buttons
response_label = tk.Label(root, text="", font=("Helvetica", 14), pady=20, 
                          bg="PeachPuff", fg="IndianRed")
response_label.pack()

# Add a decorative design using Canvas below the buttons
canvas = tk.Canvas(root, width=340, height=50, bg="PeachPuff", highlightthickness=0)
canvas.pack()

# Draw a simple design on the canvas (a line and some shapes)
canvas.create_line(20, 50, 320, 50, fill="IndianRed", width=3)
canvas.create_oval(140, 30, 200, 90, outline="IndianRed", width=2)

# Run the application
root.mainloop()
