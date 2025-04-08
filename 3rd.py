import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def get_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Waheguru89#',
            database='Data'
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Connection Error", f"Error: {err}")
        return None

def enter_data():
    accepted = accept_var.get()
    
    if accepted == "Accepted":
        name = name_entry.get()
        id = id_entry.get()
        
        if name and id:
            room = room_entry.get()
            contact = contact_entry.get()
            mail = mail_entry.get()
            course = course_combobox.get()
            branch = branch_combobox.get()
            semester = semester_spinbox.get()

            try:
                conn = get_mysql_connection()
                if conn is None:
                    return

                cursor = conn.cursor()
                
                # Create Table if it doesn't exist
                table_create_query = '''
                    CREATE TABLE IF NOT EXISTS student (
                        Name VARCHAR(50), 
                        ID INT, 
                        Room INT, 
                        Contact INT, 
                        Gmail VARCHAR(100), 
                        Course VARCHAR(100), 
                        Branch VARCHAR(100), 
                        Semester INT
                    )
                '''
                cursor.execute(table_create_query)
                
                # Insert Data
                data_insert_query = '''INSERT INTO student 
                (Name, ID, Room, Contact, Gmail, Course, Branch, Semester) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
                
                data_insert_tuple = (name, id, room, contact, mail, course, branch, semester)
                cursor.execute(data_insert_query, data_insert_tuple)
                
                conn.commit()
                messagebox.showinfo("Success", "Data entered successfully!")
                
            except mysql.connector.Error as error:
                messagebox.showerror("Database Error", str(error))
            finally:
                cursor.close()
                conn.close()
        else:
            tkinter.messagebox.showwarning(title="Error", message="Name and ID are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms.")


# Initialize the window
window2 = tkinter.Tk()
window2.title("Membership Form")
window2.configure(bg="PeachPuff")

frame = tkinter.Frame(window2, bg="PeachPuff")
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="Student Information", bg="PeachPuff", fg="Black")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

name_label = tkinter.Label(user_info_frame, text="Name", bg="PeachPuff", fg="IndianRed")
name_label.grid(row=0, column=0)
id_label = tkinter.Label(user_info_frame, text="Roll No.", bg="PeachPuff", fg="IndianRed")
id_label.grid(row=0, column=1)

name_entry = tkinter.Entry(user_info_frame)
id_entry = tkinter.Entry(user_info_frame)
name_entry.grid(row=1, column=0)
id_entry.grid(row=1, column=1)

room_label = tkinter.Label(user_info_frame, text="Room No.", bg="PeachPuff", fg="IndianRed")
room_entry = ttk.Entry(user_info_frame)
room_label.grid(row=0, column=2)
room_entry.grid(row=1, column=2)

contact_label = tkinter.Label(user_info_frame, text="Contact", bg="PeachPuff", fg="IndianRed")
contact_entry = tkinter.Entry(user_info_frame)
contact_label.grid(row=2, column=0)
contact_entry.grid(row=3, column=0)

mail_label = tkinter.Label(user_info_frame, text="Gmail", bg="PeachPuff", fg="IndianRed")
mail_entry = ttk.Entry(user_info_frame)
mail_label.grid(row=2, column=1)
mail_entry.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
course_frame = tkinter.LabelFrame(frame, bg="PeachPuff", fg="IndianRed")
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

course_label = tkinter.Label(course_frame, text="Course", bg="PeachPuff", fg="IndianRed")
course_combobox = ttk.Combobox(course_frame, values=[
    "Bachelor of Technology(Btech)", "Bachelor of Arts (BA)", "Bachelor of Science (B.Sc) - Medical", 
    "Bachelor of Science (B.Sc) - Non-Medical", "Bachelor of Science (B.Sc) - Biotechnology", 
    "Bachelor of Science (B.Sc) - Computer Science", "Bachelor of Commerce (B.Com)", 
    "Bachelor of Business Administration (BBA)", "Bachelor of Computer Applications (BCA)", 
    "Bachelor of Physiotherapy (BPT)", "Bachelor of Design (B.Des)", 
    "Bachelor of Hotel Management and Catering Technology (BHMCT)", "Master of Science (M.Sc) - Biotechnology", 
    "Master of Science (M.Sc) - Chemistry", "Master of Science (M.Sc) - Physics", 
    "Master of Science (M.Sc) - Information Technology", "Master of Arts (MA) - English", 
    "Master of Arts (MA) - Political Science", "Master of Arts (MA) - Geography", "Master of Arts (MA) - Punjabi", 
    "Master of Commerce (M.Com)", "Master of Tourism Management (MTM)"])

course_label.grid(row=0, column=0)
course_combobox.grid(row=1, column=0)

branch_label = tkinter.Label(course_frame, text="Branch", bg="PeachPuff", fg="IndianRed")
branch_combobox = ttk.Combobox(course_frame, values=["", "Computer Science", "IT", "Mechanical Engineering", 
    "Electrical Engineering", "Electronics and Communication Engineering", "Civil Engineering", 
    "Chemical Engineering", "Nursing", "Pharmacy", "LAW", "Business Administration", "Finance", 
    "Marketing", "Human Resource Management", "International Business", "Operations Management", 
    "Entrepreneurship", "Supply Chain Management", "Business Analytics"])

branch_label.grid(row=0, column=1)
branch_combobox.grid(row=1, column=1)

semester_label = tkinter.Label(course_frame, text=" Semester", bg="PeachPuff", fg="IndianRed")
semester_spinbox = tkinter.Spinbox(course_frame, from_=0, to=8)
semester_label.grid(row=0, column=2)
semester_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions", bg="PeachPuff", fg="Black")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", bg="PeachPuff", fg="IndianRed", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter Data", command=enter_data, bg="IndianRed", fg="PeachPuff")
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window2.mainloop()
