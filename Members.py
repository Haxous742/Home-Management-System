# from tkinter import *
# from tkinter import messagebox
# import csv

# FILE_NAME = "Members.csv"



# # Login Page
# def login_page():
#     def verify_credentials():
#         username = username_entry.get().strip()
#         Password = password_entry.get().strip()
#         Address = address_entry.get().strip()
#         House = house_entry.get().strip()

#         try:
#             with open(FILE_NAME, "r") as file:
#                 reader = csv.reader(file)
#                 for row in reader:
#                     if row and row[0] == username and row[1] == Password and row[3] == Address and row[4] == House:
#                         user_type = row[2]
#                         root.destroy()
#                         home_dashboard(username, user_type, Address, House)
#                         return
#                 messagebox.showerror("Error", "Invalid credentials. Please try again.")
#         except FileNotFoundError:
#             messagebox.showerror("Error", "No users registered yet!")

#     def open_register():
#         root.destroy()
#         register_page()

#     def toggle_password():
#         if password_entry.cget("show") == "*":
#             password_entry.config(show="")
#         else:
#             password_entry.config(show="*")

#     root = Tk()
#     root.title("Home Automation - Login")
#     root.geometry("400x400")
#     root.configure(bg="#202124")

#     Label(root, text="Home Automation Login", font=("Arial", 18, "bold"), fg="white", bg="#202124").pack(pady=10)

#     # Username
#     Label(root, text="Username:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     username_entry = Entry(root, width=30, bg="#303134", fg="white", insertbackground="white")
#     username_entry.pack(pady=5, padx=20)

#     # Password
#     Label(root, text="Password:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     password_entry = Entry(root, width=30, bg="#303134", fg="white", show="*", insertbackground="white")
#     password_entry.pack(pady=5, padx=20)

#     # Address
#     Label(root, text="Address:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     address_entry = Entry(root, width=30, bg="#303134", fg="white", insertbackground="white")
#     address_entry.pack(pady=5, padx=20)

#     # House
#     Label(root, text="House:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     house_entry = Entry(root, width=30, bg="#303134", fg="white", insertbackground="white")
#     house_entry.pack(pady=5, padx=20)

#     # Show password toggle
#     Checkbutton(root, text="Show password", command=toggle_password, bg="#202124", fg="white", selectcolor="#202124").pack()

#     # Login button
#     Button(root, text="Login", command=verify_credentials, bg="#5e5ce6", fg="white", width=20).pack(pady=10)

#     # Register button
#     Button(root, text="Register", command=open_register, bg="#5e5ce6", fg="white", width=20).pack()

#     root.mainloop()

# # Registration Page
# def register_page():
#     def save_credentials():
#         username = username_entry.get().strip()
#         Password = password_entry.get().strip()
#         user_type = user_type_var.get()
#         Address = address_entry.get().strip()
#         House = house_entry.get().strip()

#         if not username or not Password or not Address or not House:
#             messagebox.showwarning("Warning", "Please fill out all fields!")
#             return

#         try:
#             with open(FILE_NAME, "a", newline="") as file:
#                 writer = csv.writer(file)
#                 writer.writerow([username, Password, user_type, Address, House])
#             messagebox.showinfo("Success", "Registration Successful!")
#             root.destroy()
#             login_page()
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def toggle_password():
#         if password_entry.cget("show") == "*":
#             password_entry.config(show="")
#         else:
#             password_entry.config(show="*")

#     root = Tk()
#     root.title("Home Automation - Register")
#     root.geometry("400x450")
#     root.configure(bg="#202124")

#     Label(root, text="Register for Home Automation", font=("Arial", 18, "bold"), fg="white", bg="#202124").pack(pady=10)

#     # Username
#     Label(root, text="Username:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     username_entry = Entry(root, width=30, bg="#303134", fg="white", insertbackground="white")
#     username_entry.pack(pady=5, padx=20)

#     # Password
#     Label(root, text="Password:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     password_entry = Entry(root, width=30, bg="#303134", fg="white", show="*", insertbackground="white")
#     password_entry.pack(pady=5, padx=20)

#     # Address
#     Label(root, text="Address:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     address_entry = Entry(root, width=30, bg="#303134", fg="white", insertbackground="white")
#     address_entry.pack(pady=5, padx=20)

#     # House
#     Label(root, text="House:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     house_entry = Entry(root, width=30, bg="#303134", fg="white", insertbackground="white")
#     house_entry.pack(pady=5, padx=20)

#     # User Type
#     Label(root, text="User Type:", fg="white", bg="#202124").pack(anchor=W, padx=20)
#     user_type_var = StringVar(value="user")
#     Radiobutton(root, text="User", variable=user_type_var, value="user", bg="#202124", fg="white", selectcolor="#202124").pack(anchor=W, padx=30)
#     Radiobutton(root, text="Admin", variable=user_type_var, value="admin", bg="#202124", fg="white", selectcolor="#202124").pack(anchor=W, padx=30)

#     # Show password toggle
#     Checkbutton(root, text="Show password", command=toggle_password, bg="#202124", fg="white", selectcolor="#202124").pack()

#     # Register button
#     Button(root, text="Register", command=save_credentials, bg="#5e5ce6", fg="white", width=20).pack(pady=10)

#     root.mainloop()

# # Start the system with the login page
# if __name__ == "__main__":
#     login_page()

import CSV_Handler as csvh

class Members:
    Member_details = {}




