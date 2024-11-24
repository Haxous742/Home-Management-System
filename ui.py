import tkinter as tk
from tkinter import font
from tkinter import ttk as u

House_details = {
        "001": {"Name": "House 1"},
        "002": {"Name": "House 2"}
    }

class GUI:

    heading_font = ("Helvetica", 24, "bold")
    label_font = ("Helvetica", 12)
    entry_font = ("Helvetica", 12)

    def __init__(self,root,members,devices,houses):
        self.root = root
        self.memberObjs = members
        self.deviceObjs = devices
        self.houseObjs = houses

#===============================================================================================================================
    
    def welcome_page(self):

        for child in self.root.winfo_children():
            child.destroy()

        self.root.minsize(500,300)

        root  = self.root
        
        root.configure(bg='#f7f6f2') 

        heading_font = font.Font(family="Helvetica", size=24, weight="bold")
        subheading_font = font.Font(family="Helvetica", size=14)
        button_font = font.Font(family="Helvetica", size=12, weight="bold")

        heading_label = tk.Label(root, text="Welcome", font=heading_font, bg='#f7f6f2', fg='#1f3340')
        heading_label.pack(pady=20)

        subheading_label = tk.Label(root, text="Seamless Living, Smart Control", font=subheading_font, bg='#f7f6f2', fg='#3a536b')
        subheading_label.pack(pady=10)

        def login():
            self.login_page()
            print("Login button clicked")

        def signup():
            self.SignUp_page()
            print("Signup button clicked")

        button_frame = tk.Frame(root, bg='#f7f6f2')
        button_frame.pack(pady=40)

        button_style = {
            'font': button_font,
            'bg': '#6a8d92',  
            'fg': 'white',
            'activebackground': '#587376',  
            'activeforeground': 'white',
            'bd': 0, 
            'padx': 30,
            'pady': 10
        }

        login_button = tk.Button(button_frame, text="Login", **button_style, command=login)
        login_button.pack(side="left", padx=10)  

        signup_button = tk.Button(button_frame, text="Signup", **button_style, command=signup)
        signup_button.pack(side="left", padx=10)  
        
#==================================================================================================================================

    def SignUp_page(self):

        for child in self.root.winfo_children():
            child.destroy()

        self.root.minsize(500,470)

        root = self.root

        heading_label = tk.Label(root, text="Sign Up", font=GUI.heading_font, bg='#f7f6f2', fg='#1f3340')
        heading_label.pack(pady=20)

        input_frame = tk.Frame(root, bg='#f7f6f2')
        input_frame.pack(pady=10)

        username_label = tk.Label(input_frame, text="Username", font=GUI.label_font, bg='#f7f6f2', fg='#3a536b')
        username_label.grid(row=0, column=0, pady=5, sticky="w")
        username_entry = tk.Entry(input_frame, font=GUI.entry_font, width=30, bd=2, relief="groove")  
        username_entry.grid(row=1, column=0, pady=5)

        password_label = tk.Label(input_frame, text="Password", font=GUI.label_font, bg='#f7f6f2', fg='#3a536b')
        password_label.grid(row=2, column=0, pady=5, sticky="w")
        password_entry = tk.Entry(input_frame, font=GUI.entry_font, width=30, bd=2, relief="groove", show="*") 
        password_entry.grid(row=3, column=0, pady=5)

        address_label = tk.Label(input_frame, text="Address", font=GUI.label_font, bg='#f7f6f2', fg='#3a536b')
        address_label.grid(row=4, column=0, pady=5, sticky="w")
        address_entry = tk.Entry(input_frame, font=GUI.entry_font, width=30, bd=2, relief="groove")  
        address_entry.grid(row=5, column=0, pady=5)

        def sign_up():
            username = username_entry.get()
            password = password_entry.get()
            address = address_entry.get()
            
            print(f"Username: {username}\nPassword: {password}\nAddress: {address}")

        def go_back():
            self.welcome_page()
            print("Back to login page")

        button_style = {
            'font': font.Font(family="Helvetica", size=12, weight="bold"),
            'bg': '#6a8d92',  
            'fg': 'white',
            'activebackground': '#587376',
            'activeforeground': 'white',
            'bd': 0,
            'padx': 30,
            'pady': 10
        }

        signup_button = tk.Button(root, text="Sign Up", **button_style, command=sign_up)
        signup_button.pack(pady=15)

        back_button = tk.Button(root, text="Back", **button_style, command=go_back)
        back_button.pack(pady=10)


#=========================================================================================================================

    def login_page(self):
        
        root = self.root

        for child in root.winfo_children():
            child.destroy()
 
        self.root.minsize(500,400)  ##(hori,vertical)
        self.root.maxsize(500,400)

        heading_label = tk.Label(root, text="Login", font=GUI.heading_font, bg='#f7f6f2', fg='#1f3340')
        heading_label.pack(pady=20)

        input_frame = tk.Frame(root, bg='#f7f6f2')
        input_frame.pack(pady=10)

        username_label = tk.Label(input_frame, text="Username", font=GUI.label_font, bg='#f7f6f2', fg='#3a536b')
        username_label.grid(row=0, column=0, pady=5, sticky="w")
        username_entry = tk.Entry(input_frame, font=GUI.entry_font, width=30, bd=2, relief="groove")  
        username_entry.grid(row=1, column=0, pady=5)

        password_label = tk.Label(input_frame, text="Password", font=GUI.label_font, bg='#f7f6f2', fg='#3a536b')
        password_label.grid(row=2, column=0, pady=5, sticky="w")
        password_entry = tk.Entry(input_frame, font=GUI.entry_font, width=30, bd=2, relief="groove", show="*") 
        password_entry.grid(row=3, column=0, pady=5)

        def login():
            username = username_entry.get()
            password = password_entry.get()

            # if username == "Vedant" and password == "123":
            self.Houses_page(House_details)
            
            print(f"Username: {username}\nPassword: {password}")

        
        def go_back():
            self.welcome_page()
            print("Back to login page")
        
        button_style = {
            'font': font.Font(family="Helvetica", size=12, weight="bold"),
            'bg': '#6a8d92',  
            'fg': 'white',
            'activebackground': '#587376',
            'activeforeground': 'white',
            'bd': 0,
            'padx': 30,
            'pady': 10
        }

        login_button = tk.Button(root, text="Login", **button_style, command=login)
        login_button.pack(pady=15)

        back_button = tk.Button(root, text="Back", **button_style, command=go_back)
        back_button.pack(pady=10)

#==========================================================================================================================

    def Houses_page(self,House_details):
        root = self.root

        for child in root.winfo_children():
            child.destroy()

        root.minsize(650,370)
        root.maxsize(650,370)

        self.House_dict = House_details
        
        self.canvas = tk.Canvas(root, bg = "#f6f4ee")
        self.canvas.pack(side="left",fill="both",expand=True)

        self.scrollbar = u.Scrollbar(root,orient="vertical",command=self.canvas.yview)
        self.scrollbar.pack(side="right",fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        #main frame
        self.main_frame = tk.Frame(self.canvas, bg="#f6f4ee")
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        self.main_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        #sidebar frame
        self.sidebar = tk.Frame(self.main_frame,bg="#ffffff", width=200, height=10, bd=2, relief="solid",pady=50)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.content_frame = tk.Frame(self.main_frame, bg="#f6f4ee")
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        
        button_style = {'font': ('Helvetica', 12, 'bold'),'bg': "#7a9a9d",'fg': 'white','activebackground': "#607b7d",
            'activeforeground': 'white','bd': 1,'relief': 'solid','padx': 10,'pady': 10 }
        
        ##functions for buttons
        def add_house():
            self.Add_house_page()

        def delete_house():
            self.Remove_House_page(self.House_dict)

        def update_house():
            self.Update_House_page()

        def clear_main_content():
            for widget in self.content_frame.winfo_children():
                widget.destroy()

        def show_all_houses():
            clear_main_content()

            label = tk.Label(self.content_frame, text="All Houses:", font=('Helvetica', 16, 'bold'), bg="#f6f4ee", fg="#3c5361")
            label.pack(pady=10)

            for house_id, house_info in self.House_dict.items():
                house_frame = tk.Frame(self.content_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
                house_frame.pack(fill="x", padx=10, pady=10)

                house_text = f"House ID: {house_id}, Name: {house_info['Name']}"
                house_label = tk.Label(house_frame, text=house_text, font=('Helvetica', 12), bg="#ffffff", anchor="w", fg="#3c5361")
                house_label.pack(side="left", fill="x", expand=True, padx=10, pady=10)

                go_button = tk.Button(house_frame, text="GO", font=('Helvetica', 10, 'bold'), fg= "white" , bg="#7a9a9d",bd=1, activeforeground="white", activebackground= "#607b7d", relief= "solid" ,
                                    command=lambda house_id=house_id: go_to_house(house_id))
                go_button.pack(side="right", padx=10, pady=10)

        def go_to_house(house_id):
            pass

        # Add button
        self.add_button = tk.Button(self.sidebar, text="Add", **button_style, command=add_house)
        self.add_button.pack(fill="x", pady=5, padx=20)

        # Delete button
        self.delete_button = tk.Button(self.sidebar, text="Delete", **button_style, command=delete_house)
        self.delete_button.pack(fill="x", pady=5, padx=20)

        # Update button
        self.update_button = tk.Button(self.sidebar, text="Update", **button_style, command=update_house)
        self.update_button.pack(fill="x", pady=5, padx=20)

        # Show All button
        self.show_all_button = tk.Button(self.sidebar, text="Show All", **button_style, command=show_all_houses)
        self.show_all_button.pack(fill="x", pady=5, padx=20)

        show_all_houses()

#=============================================================================================================================
    def Add_house_page(self):
        self.add_house_window = tk.Toplevel(self.root)
        self.add_house_window.title("Add House Page")
        self.add_house_window.geometry("400x300")
        self.add_house_window.config(bg="#f6f4ee") 

        name_label = tk.Label(self.add_house_window, text="House Name:", font=("Helvetica", 12), bg="#f6f4ee", fg="#3c5361")
        name_label.pack(pady=10)
        
        self.name_entry = tk.Entry(self.add_house_window, font=("Helvetica", 12), bd=2, relief="solid", width=30)
        self.name_entry.pack(pady=5)

        section_label = tk.Label(self.add_house_window, text="Select Section:", font=("Helvetica", 12), bg="#f6f4ee", fg="#3c5361")
        section_label.pack(pady=10)
        
        self.section_var = tk.StringVar(self.add_house_window)
        self.section_var.set("Select Section")  
        
        # Define options for the dropdown
        sections = ["Bedroom", "Kitchen", "Garage", "Living room", "Bathroom"]
        
        self.section_dropdown = u.Combobox(self.add_house_window, textvariable= self.section_var, values=sections, state="readonly", font=("Helvetica", 12))
        self.section_dropdown.pack(pady=5)

        @staticmethod
        def add_section():
            selected_section = self.section_var.get()
            if selected_section != "Select Section":
                print(f"Section added: {selected_section}")
                # You can implement the logic here to add the section to the house or store the data

        
        add_button = tk.Button(self.add_house_window, text="Add", command=add_section,
                               font=("Helvetica", 12, "bold"), bg="#7a9a9d", fg="white", 
                               activebackground="#607b7d", activeforeground="white", bd=0, padx=10, pady=5)
        add_button.pack(pady=10)

        done_button = tk.Button(self.add_house_window, text="Done", command=self.add_house_window.destroy,
                                font=("Helvetica", 12, "bold"), bg="#7a9a9d", fg="white", 
                                activebackground="#607b7d", activeforeground="white", bd=0, padx=5, pady=5)
        done_button.pack(pady=10)

        
#=============================================================================================================================
    def Remove_House_page(self,House_Details):
        self.House_dict = House_Details
        self.remove_house_window = tk.Toplevel(self.root)
        self.remove_house_window.title("Remove House Page")
        self.remove_house_window.geometry("400x250")
        self.remove_house_window.config(bg="#f6f4ee")  

        select_house_label = tk.Label(self.remove_house_window, text="Select House:", font=("Helvetica", 12), bg="#f6f4ee", fg="#3c5361")
        select_house_label.pack(pady=10)

        self.selected_house_var = tk.StringVar(self.remove_house_window)
        self.selected_house_var.set("Select House")  

        house_options = [house_info["Name"] for house_info in self.House_dict.values()]

        self.house_dropdown = u.Combobox(self.remove_house_window, textvariable=self.selected_house_var, values=house_options, state="readonly", font=("Helvetica", 12))
        self.house_dropdown.pack(pady=10)

        @staticmethod
        def remove_selected_house():
            selected_house = self.selected_house_var.get()
            if selected_house != "Select House":
                print(f"House removed: {selected_house}")

        remove_button = tk.Button(self.remove_house_window, text="Remove", command=remove_selected_house,
                                  font=("Helvetica", 12, "bold"), bg="#7a9a9d", fg="white", 
                                  activebackground="#607b7d", activeforeground="white", bd=0, padx=10, pady=5)
        remove_button.pack(pady=10)

        done_button = tk.Button(self.remove_house_window, text="Done", command=self.remove_house_window.destroy,
                                font=("Helvetica", 12, "bold"), bg="#7a9a9d", fg="white", 
                                activebackground="#607b7d", activeforeground="white", bd=0, padx=10, pady=5)
        done_button.pack(pady=20)

#===============================================================================================================================

    def Update_House_page(self):

        self.update_house_window = tk.Toplevel(self.root)
        self.update_house_window.title("Update House Page")
        self.update_house_window.geometry("600x300")
        self.update_house_window.config(bg="#f6f4ee") 

        update_name_label = tk.Label(self.update_house_window, text="Update House Name:", font=("Helvetica", 12), bg="#f6f4ee", fg="#3c5361")
        update_name_label.pack(pady=10)
        
        self.update_name_entry = tk.Entry(self.update_house_window, font=("Helvetica", 12), bd=2, relief="solid", width=30)
        self.update_name_entry.pack(pady=5)

        new_section_frame = tk.Frame(self.update_house_window, bg="#f6f4ee")
        new_section_frame.pack(pady=10)

        new_section_label = tk.Label(new_section_frame, text="Add New Section:", font=("Helvetica", 12), bg="#f6f4ee", fg="#3c5361")
        new_section_label.grid(row=0, column=0, padx=5)

        self.new_section_var = tk.StringVar(self.update_house_window)
        self.new_section_var.set("Select Section")  

        # Define options for the dropdown
        sections = ["Bedroom", "Kitchen", "Garage", "Living room", "Bathroom"]
        
        self.new_section_dropdown = u.Combobox(new_section_frame, textvariable=self.new_section_var, values=sections, state="readonly", font=("Helvetica", 12))
        self.new_section_dropdown.grid(row=0, column=1, padx=5)\
        
        @staticmethod
        def add_new_section():
            selected_section = self.new_section_var.get()
            if selected_section != "Select Section":
                print(f"New section added: {selected_section}")

        # Add button beside the new section dropdown
        add_button = tk.Button(new_section_frame, text="Add", command=add_new_section,
                               font=("Helvetica", 12, "bold"), bg="#7a9a9d", fg="white", 
                               activebackground="#607b7d", activeforeground="white", bd=0, padx=10, pady=5)
        add_button.grid(row=0, column=2, padx=5)

        existing_section_frame = tk.Frame(self.update_house_window, bg="#f6f4ee")
        existing_section_frame.pack(pady=10)

        existing_section_label = tk.Label(existing_section_frame, text="Remove Section:", font=("Helvetica", 12), bg="#f6f4ee", fg="#3c5361")
        existing_section_label.grid(row=0, column=0, padx=5)
        
        self.existing_section_var = tk.StringVar(self.update_house_window)
        self.existing_section_var.set("Select Section")  

        # Pre-existing sections from the house data (for demonstration, using a sample list)
        existing_sections = ["Bedroom", "Living room", "Garage"]
        
        self.existing_section_dropdown = u.Combobox(existing_section_frame, textvariable=self.existing_section_var, values=existing_sections, state="readonly", font=("Helvetica", 12))
        self.existing_section_dropdown.grid(row=0, column=1, padx=5)
        
        @staticmethod
        def remove_existing_section():
            selected_section = self.existing_section_var.get()
            if selected_section != "Select Section":
                print(f"Section removed: {selected_section}")  

        remove_button = tk.Button(existing_section_frame, text="Del ", command=remove_existing_section,
                                  font=("Helvetica", 12, "bold"), bg="#7a9a9d", fg="white", 
                                  activebackground="#607b7d", activeforeground="white", bd=0, padx=10, pady=5)
        remove_button.grid(row=0, column=4, padx=5)

        done_button = tk.Button(self.update_house_window, text="Done", command=self.update_house_window.destroy,
                                font=("Helvetica", 12, "bold"), bg="#7a9a9d", fg="white", 
                                activebackground="#607b7d", activeforeground="white", bd=0, padx=10, pady=5)
        done_button.pack(pady=20)

#=================================================================================================================================

    def Main_Dashboard(self):
        pass

#=======================================================================================================================================
root = tk.Tk()
root.title("Home Management System")
root.geometry("500x300")
root.config(bg="#f5f5f5")

kinterobj = GUI(root,0,0,0)
kinterobj.welcome_page()

root.mainloop()
