import tkinter as tk
from tkinter import ttk

# Function to handle the button click
def done_action():
    book_name = combo_book_name.get()
    book_id = entry_book_id.get()
    selected_action = action.get()
    
    # Determine the action text
    if selected_action == 1:
        action_text = "Issue"
    elif selected_action == 2:
        action_text = "Return"
    elif selected_action == 3:
        action_text = "Reissue"
    else:
        action_text = "No action selected"
    
    # Display the input values in the output box (tk.Text)
    output_text = f"Book Name: {book_name}\nBook ID: {book_id}\nAction: {action_text}\n\nNOTE: Take screenshot or show this screen to your teacher for confirmation"
    output_box.config(state='normal')  # Allow editing to insert text
    output_box.delete(1.0, tk.END)     # Clear previous content
    output_box.insert(tk.END, output_text)  # Insert new content
    output_box.config(state='disabled')  # Disable editing again

# Create the main window
root = tk.Tk()

# Set the size of the window
root.geometry("320x440+670+100")

# Set the title of the window
root.title("Book Management System")

# Set the background color of the window
root.config(bg='peachpuff')

# Add labels for Book Name, Book ID, and Action
label_book_name = tk.Label(root, text="BOOK NAME", font=('Arial', 12,"bold"), bg='peachpuff',fg="IndianRed", anchor='w')
label_book_name.place(x=20, y=52)

label_book_id = tk.Label(root, text="BOOK ID", font=('Arial', 12,"bold"), bg='peachpuff',fg="IndianRed", anchor='w')
label_book_id.place(x=20, y=104)

label_action = tk.Label(root, text="ACTION", font=('Arial', 12,"bold"), bg='peachpuff',fg="IndianRed", anchor='w')
label_action.place(x=20, y=150)

# Add an entry box for Book Name
combo_book_name = ttk.Combobox(root, width=20)
combo_book_name.place(x=110, y=50)

# Add an entry box for Book ID
entry_book_id = tk.Entry(root, width=20)
entry_book_id.place(x=110, y=100)

# Variable to hold the selected action
action = tk.IntVar()

# Add radio buttons for Issue, Return, Reissue in front of the "Action" label
radio_issue = tk.Radiobutton(root, text="Issue", variable=action, value=1, bg='peachpuff',fg="IndianRed")
radio_issue.place(x=110, y=150)

radio_return = tk.Radiobutton(root, text="Return", variable=action, value=2, bg='peachpuff',fg="IndianRed")
radio_return.place(x=110, y=175)

radio_reissue = tk.Radiobutton(root, text="Reissue", variable=action, value=3, bg='peachpuff',fg="IndianRed")
radio_reissue.place(x=110, y=200)

# Adding done button
done_button = tk.Button(root, text="Done",fg="IndianRed", command=done_action)
done_button.place(x=130, y=250)

# Create a frame to hold the output below the Done button
output_frame = tk.Frame(root, bg='peachpuff', width=280, height=100)
output_frame.place(x=30, y=300)

# Create a Text widget to display the output
output_box = tk.Text(output_frame, height=6, width=36, font=('Arial', 12),fg="IndianRed", wrap='word')
output_box.pack()

# Disable editing for the output box (read-only mode)
output_box.config(state='disabled')

# Run the application
root.mainloop()
