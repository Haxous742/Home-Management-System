import customtkinter as ctk
import tkinter as TK
from tkinter import messagebox , Scrollbar , Canvas
import csv as csv
import CSV_Handler as csvh
from PIL import Image, ImageTk
import os
import requests
from io import BytesIO
import colorsys
import Houses as House
import Devices as Device
import HomeManager as hm
import math
import Status_Report as st


Member_details = {
        "Vedant" : {"Password":"123" , "Address" :"IRIS"}
    } 

Device_Details = {
                  "B01" : {"name" : "Bulb_1", "type" : "bulb", "status" : "on" , "attributes":{"brightness":"69","colour":"green"}},
                  "T01" : {"name" : "Thermostat_1", "type":"thermostat", "status":"On", "attributes":{"brightness":"69","colour":"green"}}, 
                  "T02" : {"name" : "Thermostat_2", "type":"thermostat", "status":"On", "attributes":{"brightness":"69","colour":"green"}},
                  "C01" : {"name" : "Porch_CCTV", "type":"cctv", "status":"On", "attributes":{"brightness":"69","colour":"green"}},
                  "O01" : {"name" : "Oven_kitchen", "type":"oven", "status":"On", "attributes":{"brightness":"69","colour":"green"}},
                  "F01" : {"name" : "Fridge_hall", "type":"fridge", "status":"On", "attributes":{"brightness":"69","colour":"green"}},
                }

  
House_details = {
            "Vedant" : {"data" : [["Bedroom01","Bedroom",("B01","bulb"),("T01","thermostat"),("F01","fridge")],["Garage01","Garage",("T02","thermostat"),("O01","oven"),("C01","cctv")]]}
            }

    #Code:
    #Bulb : B
    #CCTV : C
    #Thermostat : T
    #Oven : O
    #Fridge : F
    #ChargingStation : S
    #GarageDoor : G

    #user - house object
    #user.Section_list = []
    #section.Device_list


class GUI:

    def __init__(self,app,MemberDict,Housedict,Devicedict):
        self.app = app
        self.Member_details = MemberDict
        self.House_details = Housedict
        self.Device_details = Devicedict
        self.userobj = House.Houses()


    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

#==================================================================================================================================
  #STATIC METHODS

    @staticmethod
    def toggle_password(entry, check_var):
        if check_var.get():
            entry.configure(show="")
        else:
            entry.configure(show="*")

    @staticmethod
    def vanish_cursor(entry):
        def on_focus_out(event):
            if entry.get() != "":
                entry.configure(insertbackground=entry.cget("fg_color")) 
        entry.bind("<FocusOut>", on_focus_out)

#==============================================================================================================================================

    def show_login(self):
        
        app = self.app

        for widget in app.winfo_children():
            widget.destroy()

        app.minsize(400,430)
        app.maxsize(400,430)

        def execute(username):

            self.userobj.Username_update(username)

            for keys in self.House_details:
                if (keys == username):
                    user1 = username

            for secs in self.House_details[user1]["data"]:

                if (secs[1]=="Bedroom"):
                    exec(f"temp_s = House.Bedroom(secs[0])")

                elif (secs[1]=="Kichen"):
                    exec(f"temp_s = House.Kitchen(secs[0])")

                elif (secs[1]=="Garage"):
                    exec(f"temp_s = House.Garage(secs[0])")

                elif (secs[1]=="LivingRoom"):
                    exec(f"temp_s = House.LivingRoom(secs[0])")

                elif (secs[1]=="Bathroom"):
                    exec(f"temp_s= House.Bathroom(secs[0])")

                exec("self.userobj.Section_list.append(temp_s)")

                for i in range(2,len(secs)):

                    for ids in self.Device_details.keys():
                        if (ids == secs[i][0]):
                            id = ids
                            device_name = self.Device_details[id]["name"]

                    if (secs[i][1]=="bulb"):
                        exec(f"temp_d = Device.Bulb(device_name)")

                    elif (secs[i][1]=="thermostat"):
                        exec(f"temp_d = Device.Thermostat(device_name)")

                    elif (secs[i][1] == "cctv"):
                        exec(f"temp_d = Device.Security_camera(device_name)")

                    elif (secs[i][1] == "fridge"):
                        exec(f"temp_d = Device.Refrigerator(device_name)")

                    elif (secs[i][1] == "oven"):
                        exec(f"temp_d = Device.Oven(device_name)")

                    elif (secs[i][1] == "chargingstation"):
                        exec(f"temp_d  = Device.Charging_hub(device_name)")

                    exec("temp_d.update_id(id)")

                    exec('''if temp_d.type == "fridge":
                                temp_d.make_objs()         
                                                    ''')
                    def init_devices(obj):
                        self.Device_details = csvh.CSV_Handler.loadDevices()

                        for keys in self.Device_details.keys():
                            if (keys == obj.device_id):
                                obj.updateStatus(self.Device_details[keys]["status"])

                                if obj.type == "bulb":

                                    obj.updateBrightness(math.floor(float(self.Device_details[keys]["attributes"]["Brightness"])))
                                    obj.updateWarmth(math.floor(float(self.Device_details[keys]["attributes"]["Warmth"]))) 
                                    obj.updateColour(math.floor(float(self.Device_details[keys]["attributes"]["Colour"])))
                                
                                elif obj.type == "thermostat":

                                    obj.updateTemperature(int(self.Device_details[keys]["attributes"]["Temperature"]))
                                    obj.updateMode(self.Device_details[keys]["attributes"]["Mode"])

                                elif obj.type == "cctv":
                                    
                                    obj.updateResolution(self.Device_details[keys]["attributes"]["Resolution"])
                                    obj.updateMode(self.Device_details[keys]["attributes"]["Mode"])

                                elif obj.type == "oven":

                                    obj.updateTemperature(int(self.Device_details[keys]["attributes"]["Temperature"]))
                                    obj.updateMode(self.Device_details[keys]["attributes"]["Mode"])

                                # else:
                                        #fridge
                    
                    exec("init_devices(temp_d)")

                    exec("temp_s.Device_list.append(temp_d)")

                    self.House_details = csvh.CSV_Handler.loadHouses()
                    self.Device_details = csvh.CSV_Handler.loadDevices()

        def verify_credentials():
            username = username_entry.get().strip()
            Password = password_entry.get().strip()

            if not username or not Password:
                messagebox.showwarning("Warning", "Please fill out all fields!")
                return

            try:
                Member_details = self.Member_details
                print(Member_details)
                for key in Member_details:
                    if key == username:
                        if Member_details[key]["Password"] == Password:
                            execute(username)
                            for widget in app.winfo_children():
                                widget.destroy()
                            self.MainDashboard()
                            return 
                messagebox.showerror("Error", "Invalid Username or Password. Please try again.")
            except FileNotFoundError:
                messagebox.showerror("Error", "No users registered yet!")

        login_frame = ctk.CTkFrame(app, width=400, height=350, corner_radius=15, fg_color="#f4f5f7")
        login_frame.pack(pady=30)

        login_label = ctk.CTkLabel(login_frame, text="Login", font=("Arial", 24, "bold"), text_color="#333333")
        login_label.pack(pady=10)

        username_label = ctk.CTkLabel(login_frame, text="Username", font=("Arial", 16), text_color="#555555")
        username_label.pack(pady=5)
        username_entry = ctk.CTkEntry(login_frame, width=250)
        username_entry.pack(pady=5)
        self.vanish_cursor(username_entry) 

        password_label = ctk.CTkLabel(login_frame, text="Password", font=("Arial", 16), text_color="#555555")
        password_label.pack(pady=5)
        password_entry = ctk.CTkEntry(login_frame, width=250, show="*")
        password_entry.pack(pady=5)
        self.vanish_cursor(password_entry)  

        # Checkbox to show/hide password
        show_password_var = ctk.BooleanVar()
        show_password_checkbox = ctk.CTkCheckBox(login_frame, text="Show Password", variable=show_password_var, command=lambda: self.toggle_password(password_entry, show_password_var))
        show_password_checkbox.pack(pady=5)

        login_button = ctk.CTkButton(login_frame, text="Login", width=150, height=40, corner_radius=10,command=verify_credentials)
        login_button.pack(pady=(20, 10))

        back_button = ctk.CTkButton(login_frame, text="Back", width=150, height=40, corner_radius=10,command=self.show_home)
        back_button.pack()

#===================================================================================================================================================

    def show_signup(self):

        app = self.app

        for widget in app.winfo_children():
            widget.destroy()

        def save_credentials():
            username = username_entry.get().strip()
            Password = password_entry.get().strip()
            Address = address_entry.get().strip()

            if not username or not Password or not Address:
                messagebox.showwarning("Warning", "Please fill out all fields!")
                return
            
            if csvh.CSV_Handler.checkMembers(username) == 1:
                messagebox.showwarning("Error", "Username already taken!!")
                return
            
            try:
                member_dict = { username : {"Password" : Password,"Address": Address , "Houses" : []} }
                csvh.CSV_Handler.updateMembers(member_dict)
                messagebox.showinfo("Success", "Registration Successful!")
                self.Member_details = csvh.CSV_Handler.loadMembers()
                self.House_details[username] = {"data" : []}
                csvh.CSV_Handler.updateHouses(self.House_details)
                for widget in app.winfo_children():
                    widget.destroy()
                self.show_home()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        app.minsize(400,500)
        app.maxsize(400,500)

        signup_frame = ctk.CTkFrame(app, width=400, height=500, corner_radius=15, fg_color="#f4f5f7")
        signup_frame.pack(pady=30)

        signup_label = ctk.CTkLabel(signup_frame, text="Sign Up", font=("Arial", 24, "bold"), text_color="#333333")
        signup_label.pack(pady=10)

        username_label = ctk.CTkLabel(signup_frame, text="Username", font=("Arial", 16), text_color="#555555")
        username_label.pack(pady=5)
        username_entry = ctk.CTkEntry(signup_frame, width=250)
        username_entry.pack(pady=5)
        self.vanish_cursor(username_entry)  

        address_label = ctk.CTkLabel(signup_frame, text="Address", font=("Arial", 16), text_color="#555555")  # Changed from Email to Address
        address_label.pack(pady=5)
        address_entry = ctk.CTkEntry(signup_frame, width=250)
        address_entry.pack(pady=5)
        self.vanish_cursor(address_entry)  

        password_label = ctk.CTkLabel(signup_frame, text="Password", font=("Arial", 16), text_color="#555555")
        password_label.pack(pady=5)
        password_entry = ctk.CTkEntry(signup_frame, width=250, show="*")
        password_entry.pack(pady=5)
        self.vanish_cursor(password_entry)  

        show_password_var = ctk.BooleanVar()
        show_password_checkbox = ctk.CTkCheckBox(signup_frame, text="Show Password", variable=show_password_var, command=lambda: self.toggle_password(password_entry, show_password_var))
        show_password_checkbox.pack(pady=5)

        signup_button = ctk.CTkButton(signup_frame, text="Sign Up", width=150, height=40, corner_radius=10,command = save_credentials)
        signup_button.pack(pady=(20, 10))

        back_button = ctk.CTkButton(signup_frame, text="Back", width=150, height=40, corner_radius=10,command=self.show_home)  
        back_button.pack()

#==============================================================================================================================================

    def show_home(self):

        app = self.app

        for widget in app.winfo_children():
            widget.destroy()
            
        app.minsize(400,300)
        app.maxsize(400,300)

        home_frame = ctk.CTkFrame(app, width=400, height=250, corner_radius=15, fg_color="#f4f5f7")
        home_frame.pack(pady=30)

        label_title = ctk.CTkLabel(home_frame, text="Welcome", font=("Arial", 24, "bold"), text_color="#333333")
        label_title.pack(pady=(20, 10))

        label_subtitle = ctk.CTkLabel(home_frame, text="Seamless Living, Smart Control", font=("Arial", 16), text_color="#555555")
        label_subtitle.pack(pady=5)

        login_button = ctk.CTkButton(home_frame, text="Login", width=150, height=40, corner_radius=10,command=self.show_login)
        login_button.pack(pady=(30, 10))

        signup_button = ctk.CTkButton(home_frame, text="Sign Up", width=150, height=40, corner_radius=10, command=self.show_signup)
        signup_button.pack()

#===================================================================================================================================================

####
####
####                                       DEVICES
####
####

#=================================================================================================================================================================
## DEVICES

    def Bulb_setting(self, obj):
        def update_circle_color(event=None):
            hue_value = hue_slider.get() / 100
            brightness_value = brightness_slider.get() / 100
            warmth_value = warmth_slider.get() / 100

            r, g, b = colorsys.hsv_to_rgb(hue_value, brightness_value, 1)
            r += warmth_value * (1 - r)
            g += warmth_value * (1 - g)
            color = f'#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}'

            canvas.itemconfig(circle, fill=color)
            color_value_label.config(text=f"Color Value: {int(hue_value * 100)}")

        def update_brightness(event=None):
            brightness_value = brightness_slider.get() / 100
            color = f'#{int(255 * brightness_value):02x}{int(255 * brightness_value):02x}{int(255 * brightness_value):02x}'
            brightness_circle.itemconfig(brightness_display, fill=color)
            brightness_value_label.config(text=f"Brightness Value: {int(brightness_value * 100)}")

        def update_warmth(event=None):
            warmth_value = warmth_slider.get() / 100
            r = 255
            g = int(255 * (1 - warmth_value))
            color = f'#{r:02x}{g:02x}00'
            warmth_circle.itemconfig(warmth_display, fill=color)
            warmth_value_label.config(text=f"Warmth Value: {int(warmth_value * 100)}")

        def toggle_bulb_state():
            if bulb_switch.get():
                print("Bulb is ON")
            else:
                print("Bulb is OFF")

        app1 = ctk.CTk()
        app1.title("Settings of Bulb")
        app1.geometry("440x440")
        app1.configure(bg="#2C2F33")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        frame_sliders = ctk.CTkFrame(app1)
        frame_sliders.grid(row=0, column=0, padx=20, pady=20)

        # ======================== HUE SLIDER ============================
        hue_label = ctk.CTkLabel(frame_sliders, text="Color", text_color="white")
        hue_label.grid(row=0, column=0)

        hue_slider = ctk.CTkSlider(frame_sliders, from_=0, to=100, command=update_circle_color, width=200)
        hue_slider.set(obj.Colour)
        hue_slider.grid(row=1, column=0, pady=10)

        color_value_label = ctk.CTkLabel(frame_sliders, text=f"Color Value: {math.floor(obj.Colour)}", text_color="white")
        color_value_label.grid(row=2, column=0)

        canvas = ctk.CTkCanvas(frame_sliders, width=50, bg="#2C2F33", height=50, highlightthickness=0)
        canvas.grid(row=1, column=1, pady=10)
        circle = canvas.create_oval(10, 10, 40, 40, fill="#FFFF00")

        # ===================== BRIGHTNESS SLIDER ==========================
        brightness_label = ctk.CTkLabel(frame_sliders, text="Brightness", text_color="white")
        brightness_label.grid(row=3, column=0)

        brightness_slider = ctk.CTkSlider(frame_sliders, from_=0, to=100, command=update_brightness, width=200)
        brightness_slider.set(obj.Brightness)
        brightness_slider.grid(row=4, column=0, pady=10)

        brightness_value_label = ctk.CTkLabel(frame_sliders, text=f"Brightness Value: {math.floor(obj.Brightness)}", text_color="white")
        brightness_value_label.grid(row=5, column=0)

        brightness_circle = ctk.CTkCanvas(frame_sliders, width=50, bg="#2C2F33", height=50, highlightthickness=0)
        brightness_circle.grid(row=4, column=1, pady=10)
        brightness_display = brightness_circle.create_oval(10, 10, 40, 40, fill="#FFFF00")

        # ========================= WARMTH SLIDER ==========================
        warmth_label = ctk.CTkLabel(frame_sliders, text="Warmth", text_color="white")
        warmth_label.grid(row=6, column=0)

        warmth_slider = ctk.CTkSlider(frame_sliders, from_=0, to=100, command=update_warmth, width=200)
        warmth_slider.set(obj.Warmth)
        warmth_slider.grid(row=7, column=0, pady=10)

        warmth_value_label = ctk.CTkLabel(frame_sliders, text=f"Warmth Value: {math.floor(obj.Warmth)}", text_color="white")
        warmth_value_label.grid(row=8, column=0)

        warmth_circle = ctk.CTkCanvas(frame_sliders, width=50, bg="#2C2F33", height=50, highlightthickness=0)
        warmth_circle.grid(row=7, column=1, pady=10)
        warmth_display = warmth_circle.create_oval(10, 10, 40, 40, fill="#FFFF00")

        # ========================= BULB ON/OFF SWITCH ==========================
        switch_label = ctk.CTkLabel(frame_sliders, text="Switch Bulb On/Off", text_color="white")
        switch_label.grid(row=9, column=0, pady=(10, 5))

        bulb_switch = ctk.CTkSwitch(frame_sliders, text="Bulb State", command=toggle_bulb_state)
        bulb_switch.grid(row=10, column=0) 
        if obj.status == "on":
            bulb_switch.select()
        else:
            bulb_switch.deselect()

        # ======================== BULB NAME & UPDATE SECTION ===============================
        bulb_frame = ctk.CTkFrame(app1)
        bulb_frame.grid(row=0, column=2, padx=10, pady=10)

        bulb_name_label = ctk.CTkLabel(bulb_frame, text="Update Name of Bulb:", text_color="white")
        bulb_name_label.grid(row=0, column=0, pady=5)

        bulb_name_entry = ctk.CTkEntry(bulb_frame, placeholder_text="Enter bulb name")
        bulb_name_entry.grid(row=1, column=0, pady=5)

        def update(obj, app1):
            obj.updateBrightness(brightness_slider.get())
            obj.updateColour(hue_slider.get())
            obj.updateWarmth(warmth_slider.get())
            if bulb_switch.get():
                print("Bulb is ON")
                obj.updateStatus("on")
            else:
                print("Bulb is OFF")
                obj.updateStatus("off") 

            if len(bulb_name_entry.get()) > 0:
                obj.updateName(bulb_name_entry.get())

            self.MainDashboard()
            app1.destroy()

        Update_button = ctk.CTkButton(bulb_frame, text="Update", text_color="white", command=lambda: update(obj, app1))
        Update_button.grid(row=5, column=0, pady=20)

        app1.mainloop()


    def Thermostat_settings(self, obj):
        app1 = ctk.CTk()
        app1.title("Settings of Thermostat")
        app1.geometry("500x550")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        tabview = ctk.CTkTabview(app1, width=400, height=300)
        tabview.pack(pady=20, padx=20, fill="both", expand=True)

        thermostat_tab = tabview.add("Thermostat Settings")

        current_temperature = obj.Temperature
        current_mode = obj.Mode

        def switch_on_off_callback():
            if on_off_switch.get():
                print("Thermostat is ON")
            else:
                print("Thermostat is OFF")

        on_off_switch = ctk.CTkSwitch(thermostat_tab,text="Switch ON/OFF",onvalue=True,offvalue=False,command=switch_on_off_callback)
        on_off_switch.pack(pady=(10, 10))  

        if obj.status == "on":
            on_off_switch.select()
        else:
            on_off_switch.deselect()

        def update_temperature(value):
            global current_temperature
            current_temperature = int(value)
            temp_value_label.configure(text=f"Temperature: {current_temperature}°C")

        def update_mode(selected_mode):
            global current_mode
            current_mode = selected_mode

        temperature_label = ctk.CTkLabel(thermostat_tab, text="Temperature", font=("Arial", 16))
        temperature_label.pack(pady=(20, 5))

        temperature_slider = ctk.CTkSlider(thermostat_tab, from_=16, to=40, number_of_steps=84, orientation="horizontal", command=update_temperature)
        temperature_slider.pack(pady=10, padx=20)
        temperature_slider.set(current_temperature)

        temp_value_label = ctk.CTkLabel(thermostat_tab, text=f"Temperature: {current_temperature}°C", font=("Arial", 14))
        temp_value_label.pack(pady=5)

        temp_value_current_label = ctk.CTkLabel(thermostat_tab, text=f"Current Temperature: {current_temperature}°C", font=("Arial", 14))
        temp_value_current_label.pack(pady=5)

        mode_label = ctk.CTkLabel(thermostat_tab, text="Select Mode", font=("Arial", 16))
        mode_label.pack(pady=(7, 5))

        modes = ["Heat", "Cool", "Fan"]
        mode_dropdown = ctk.CTkOptionMenu(thermostat_tab, values=modes, command=update_mode)
        mode_dropdown.pack(pady=10, padx=20)
        mode_dropdown.set(current_mode)

        thermostat_name_label = ctk.CTkLabel(thermostat_tab, text="Update Name of Thermostat:", text_color="white")
        thermostat_name_label.pack(pady=(5, 5))

        thermostat_name_entry = ctk.CTkEntry(thermostat_tab, placeholder_text="Enter name")
        thermostat_name_entry.pack(pady=(5, 5))

        def update(obj, app1):
            obj.updateTemperature(math.floor(temperature_slider.get()))
            obj.updateMode(mode_dropdown.get())
            if len(thermostat_name_entry.get()) > 0:
                obj.updateName(thermostat_name_entry.get())

            print(f"Final Temperature: {current_temperature}°C")
            print(f"Final Mode: {current_mode}")
            if on_off_switch.get():
                print("Thermostat is ON")
                obj.updateStatus("on")
            else:
                print("Thermostat is OFF")
                obj.updateStatus("off")

            self.MainDashboard()
            app1.destroy()

        Update_button = ctk.CTkButton(thermostat_tab,text="Update",text_color="white",fg_color="#00b300",command=lambda: update(obj, app1))
        Update_button.pack(pady=(10, 5))

        app1.mainloop()

    def CCTV_settings(self, obj):
        app1 = ctk.CTk()
        app1.title("Settings of CCTV")
        app1.geometry("500x550")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        selected_resolution = obj.Resolution
        current_mode = obj.Mode

        def switch_on_off_callback():
            if on_off_switch.get():
                print("cctv is ON")
            else:
                print("cctv is OFF")    

        def update_resolution(selected_value):
            global selected_resolution
            selected_resolution = selected_value

        def update_mode(selected_mode):
            global current_mode
            current_mode = selected_mode

        tabview = ctk.CTkTabview(app1, width=400, height=300)
        tabview.pack(pady=20, padx=20, fill="both", expand=True)

        cctv_tab = tabview.add("CCTV Settings")

        on_off_switch = ctk.CTkSwitch(cctv_tab,text="Switch ON/OFF",onvalue=True,offvalue=False,command=switch_on_off_callback)
        on_off_switch.pack(pady=(10, 10))  

        if obj.status == "on":
            on_off_switch.select()
        else:
            on_off_switch.deselect() 

        resolution_label = ctk.CTkLabel(cctv_tab, text="Select Resolution", font=("Arial", 16))
        resolution_label.pack(pady=(20, 5))

        resolutions = ["720p", "1080p", "4K", "8K"]
        resolution_dropdown = ctk.CTkOptionMenu(cctv_tab, values=resolutions, command=update_resolution)
        resolution_dropdown.pack(pady=10, padx=20)
        resolution_dropdown.set(selected_resolution)

        recording_label = ctk.CTkLabel(cctv_tab, text="Recording Status", font=("Arial", 16))
        recording_label.pack(pady=(20, 5))

        mode_label = ctk.CTkLabel(cctv_tab, text="Select Mode", font=("Arial", 16))
        mode_label.pack(pady=(7, 5))

        modes = ["Day", "Night"]
        mode_dropdown = ctk.CTkOptionMenu(cctv_tab, values=modes, command=update_mode)
        mode_dropdown.pack(pady=10, padx=20)
        mode_dropdown.set(current_mode)

        CCTV_name_label = ctk.CTkLabel(cctv_tab, text="Update Name of Camera:", text_color="white")
        CCTV_name_label.pack(pady=(5, 5))

        CCTV_name_entry = ctk.CTkEntry(cctv_tab, placeholder_text="Enter CCTV name")
        CCTV_name_entry.pack(pady=(5, 5))

        def update(obj, app1):
            obj.updateResolution(resolution_dropdown.get())
            obj.updateMode(mode_dropdown.get())
            if on_off_switch.get():
                print("cctv is ON")
                obj.updateStatus("on")
            else:
                print("cctv is OFF")
                obj.updateStatus("off")
            if len(CCTV_name_entry.get()) > 0:
                obj.updateName(CCTV_name_entry.get())
            print(f"Final Resolution: {selected_resolution}")
            self.MainDashboard() 
            app1.destroy()

        Update_button = ctk.CTkButton(
            cctv_tab, text="Update", text_color="white", fg_color="#00b300", command=lambda: update(obj, app1)
        )
        Update_button.pack(pady=(10, 5))

        app1.mainloop()

    def ChargingStation_settings(self,obj):
       
        app1 = ctk.CTk()
        app1.title("Charging Station")
        app1.geometry("500x450")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        tabview = ctk.CTkTabview(app1, width=400, height=300)
        tabview.pack(pady=20, padx=20, fill="both", expand=True)

        charging_tab = tabview.add("Charging Station")

        battery_level = 50  # Default battery level
        charging_status = False  # Default status is Off

        def update_charging_status(value):
            global charging_status
            charging_status = value
            charging_status_label.configure(text=f"Charging Status: {'On' if charging_status else 'Off'}")

        battery_level_value_label = ctk.CTkLabel(charging_tab, text=f"Battery Level: {battery_level}%", font=("Arial", 14))
        battery_level_value_label.pack(pady=5)

        charging_status_label = ctk.CTkLabel(charging_tab, text=f"Charging Status: {'On' if charging_status else 'Off'}", font=("Arial", 14))
        charging_status_label.pack(pady=(20, 5))

        charging_switch = ctk.CTkSwitch(charging_tab,text="Turn Charging On/Off",command=lambda: update_charging_status(charging_switch.get()),)
        charging_switch.pack(pady=10, padx=20)
        charging_switch.deselect()  

        bulb_name_label = ctk.CTkLabel(charging_tab, text="Update Name of Charging Station:", text_color="white")
        bulb_name_label.pack(pady=(5,5))

        bulb_name_entry = ctk.CTkEntry(charging_tab, placeholder_text="Enter Charging Station name")
        bulb_name_entry.pack(pady=(5,5))

        section_label = ctk.CTkLabel(charging_tab, text="Update Section:", text_color="white")
        section_label.pack(pady=(5,5))

        section_options = ["Bedroom", "Bathroom"]
        section_menu = ctk.CTkOptionMenu(charging_tab, values=section_options)
        section_menu.pack(pady=(5,5))

        Update_button = ctk.CTkButton(charging_tab,text = "Update", text_color = "white" , fg_color = "#00b300")
        Update_button.pack(pady = (10,5))

        app1.mainloop()

    def Fridge_settings(self,obj):

        app1 = ctk.CTk()
        app1.title("Settings of Fridge")
        app1.geometry("500x550")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        scrollable_frame = ctk.CTkScrollableFrame(app1, width=500, height=550)
        scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tabview = ctk.CTkTabview(scrollable_frame, width=400, height=300)
        tabview.pack(pady=20, padx=20, fill="both", expand=True)

        Fridge_tab = tabview.add("Fridge Settings")

        current_temperature_fridge = obj.Fridgeobj.temperature 
        current_temperature_freezer = obj.Freezerobj.temperature
        current_humidity = obj.Fridgeobj.humidity 

        def switch_on_off_callback():
            if on_off_switch.get():
                print("Fridge is ON")
            else:
                print("Fridge is OFF")

        on_off_switch = ctk.CTkSwitch(Fridge_tab,text="Switch ON/OFF",onvalue=True,offvalue=False,command=switch_on_off_callback)
        on_off_switch.pack(pady=(10, 10))  

        if obj.status == "on":
            on_off_switch.select()
        else:
            on_off_switch.deselect()

        def update_temperature_fridge(value):
            global current_temperature_fridge
            current_temperature_fridge = int(value)
            temp_value_label_fridge.configure(text=f"Temperature: {current_temperature_fridge}°C")

        def update_temperature_freezer(value):
            global current_temperature_freezer
            current_temperature_freezer = int(value)
            temp_value_label_freezer.configure(text=f"Temperature: {current_temperature_freezer}°C")

        def update_humidity(selected_humidity):
            global current_humidity
            current_humidity = selected_humidity

        temperature_label_fridge = ctk.CTkLabel(Fridge_tab, text="Temperature of Fridge", font=("Arial", 16))
        temperature_label_fridge.pack(pady=(20, 5))

        temperature_slider_fridge = ctk.CTkSlider(Fridge_tab,from_=1,to=5,number_of_steps=84,orientation="horizontal",command=update_temperature_fridge)
        temperature_slider_fridge.pack(pady=10, padx=20)
        temperature_slider_fridge.set(current_temperature_fridge)  

        temp_value_label_fridge = ctk.CTkLabel(Fridge_tab, text=f"Temperature of Fridge: {current_temperature_fridge}°C", font=("Arial", 14))
        temp_value_label_fridge.pack(pady=5)

        temp_value_current_label_fridge = ctk.CTkLabel(Fridge_tab, text=f"Current Temperature of Fridge: {current_temperature_fridge}°C", font=("Arial", 14))
        temp_value_current_label_fridge.pack(pady=5)

        temperature_label_freezer = ctk.CTkLabel(Fridge_tab, text="Temperature of Freezer", font=("Arial", 16))
        temperature_label_freezer.pack(pady=(20, 5))

        temperature_slider_freezer = ctk.CTkSlider(Fridge_tab,from_=(-18),to=0,number_of_steps=84,orientation="horizontal",command=update_temperature_freezer)
        temperature_slider_freezer.pack(pady=10, padx=20)
        temperature_slider_freezer.set(current_temperature_freezer)  

        temp_value_label_freezer = ctk.CTkLabel(Fridge_tab, text=f"Temperature of Freezer: {current_temperature_freezer}°C", font=("Arial", 14))
        temp_value_label_freezer.pack(pady=5)

        temp_value_current_label_freezer = ctk.CTkLabel(Fridge_tab, text=f"Current Temperature of Freezer: {current_temperature_freezer}°C", font=("Arial", 14))
        temp_value_current_label_freezer.pack(pady=5)

        # Mode Dropdown
        mode_label = ctk.CTkLabel(Fridge_tab, text="Select Mode", font=("Arial", 16))
        mode_label.pack(pady=(7, 5))

        modes = ["High","Medium","Low"]
        mode_dropdown = ctk.CTkOptionMenu(Fridge_tab, values=modes, command=update_humidity)
        mode_dropdown.pack(pady=10, padx=20)
        mode_dropdown.set(current_humidity) 

        Fridge_name_label = ctk.CTkLabel(Fridge_tab, text="Update Name of Fridge:", text_color="white")
        Fridge_name_label.pack(pady=(5, 5))

        Fridge_name_entry = ctk.CTkEntry(Fridge_tab, placeholder_text="Enter name")
        Fridge_name_entry.pack(pady=(5, 5))

        def update(obj,app1):
            obj.Fridgeobj.update_temperature(math.floor(temperature_slider_fridge.get()))
            obj.Freezerobj.update_temperature(math.floor(temperature_slider_freezer.get()))
            obj.Fridgeobj.update_humidity(mode_dropdown.get())
            if len(Fridge_name_entry.get()) > 0 :
                obj.update_name(Fridge_name_entry.get())
            if on_off_switch.get():
                print("Fridge is ON")
                obj.updateStatus("on")
            else:
                print("Fridge is OFF")
                obj.updateStatus("off")

            self.MainDashboard() 
            app1.destroy()

        Update_button = ctk.CTkButton(Fridge_tab, text="Update", text_color="white", fg_color="#00b300",command = lambda : update(obj,app1))
        Update_button.pack(pady=(10, 5))

        app1.mainloop()

    def Oven_settings(self,obj):

        app1 = ctk.CTk()
        app1.title("Settings of Oven")
        app1.geometry("500x550")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        tabview = ctk.CTkTabview(app1, width=400, height=300)
        tabview.pack(pady=20, padx=20, fill="both", expand=True)

        Oven_tab = tabview.add("Oven Settings")

        current_temperature = obj.temperature  
        current_mode = obj.mode 

        def switch_on_off_callback():
            if on_off_switch.get():
                print("Oven is ON")
            else:
                print("Oven is OFF")

        on_off_switch = ctk.CTkSwitch(Oven_tab,text="Switch ON/OFF",onvalue=True,offvalue=False,command=switch_on_off_callback)
        on_off_switch.pack(pady=(10, 10))  

        if obj.status == "on":
            on_off_switch.select()
        else:
            on_off_switch.deselect()

        def update_temperature(value):
            global current_temperature
            current_temperature = int(value)
            temp_value_label.configure(text=f"Temperature: {current_temperature}°C")

        def update_mode(selected_mode):
            global current_mode
            current_mode = selected_mode

        temperature_label = ctk.CTkLabel(Oven_tab, text="Temperature", font=("Arial", 16))
        temperature_label.pack(pady=(20, 5))

        temperature_slider = ctk.CTkSlider(Oven_tab,from_=180,to=260,number_of_steps=84,orientation="horizontal",command=update_temperature,)
        temperature_slider.pack(pady=10, padx=20)
        temperature_slider.set(current_temperature)  

        temp_value_label = ctk.CTkLabel(Oven_tab, text=f"Temperature: {current_temperature}°C", font=("Arial", 14))
        temp_value_label.pack(pady=5)

        temp_value_current_label = ctk.CTkLabel(Oven_tab, text=f"Current Temperature: {current_temperature}°C", font=("Arial", 14))
        temp_value_current_label.pack(pady=5)

        mode_label = ctk.CTkLabel(Oven_tab, text="Select Mode", font=("Arial", 16))
        mode_label.pack(pady=(7, 5))

        modes = ["Boil", "Bake", "AirFry","Defrost"]
        mode_dropdown = ctk.CTkOptionMenu(Oven_tab, values=modes, command=update_mode)
        mode_dropdown.pack(pady=10, padx=20)
        mode_dropdown.set(current_mode) 

        oven_name_label = ctk.CTkLabel(Oven_tab, text="Update Name of Oven:", text_color="white")
        oven_name_label.pack(pady=(5,5))

        oven_name_entry = ctk.CTkEntry(Oven_tab, placeholder_text="Enter oven name")
        oven_name_entry.pack(pady=(5,5))

        def update(obj,app1):
            obj.updateTemperature(math.floor(temperature_slider.get()))
            obj.updateMode(mode_dropdown.get())

            if len(oven_name_entry.get()) > 0 :
                obj.updateName(oven_name_entry.get())

            if on_off_switch.get():
                print("Oven is ON")
                obj.updateStatus("on")
            else:
                print("Oven is OFF")
                obj.updateStatus("off")

            self.MainDashboard()
            app1.destroy()

        Update_button = ctk.CTkButton(Oven_tab,text = "Update", text_color = "white" , fg_color = "#00b300",command = lambda : update(obj,app1))
        Update_button.pack(pady = (10,5))

        app1.mainloop()

#====================================================================================================================================================================

    def MainDashboard(self):

        app = self.app

        for widget in app.winfo_children():
            widget.destroy()
            
        app.minsize(760,600)
        app.maxsize(760,600)


#=================================================================================================================================================

        def fetch_image_from_local(path, size):
            """
            Fetches an image from the local filesystem, resizes it, and converts it to a CTkImage.
            
            Args:
                path (str): The path to the image file.
                size (tuple): The desired size of the image (width, height).

            Returns:
                CTkImage: Resized image suitable for use in CustomTkinter.
            """
            try:
                img = Image.open(path)  # Open the image from the local path
                img = img.resize(size)  # Resize the image
                return ctk.CTkImage(light_image=img, dark_image=img, size=size)  # Return a CTkImage
            except Exception as e:
                print(f"Error loading image from {path}: {e}")
                return None  # Return None if there's an error

        image_folder = "images"  
        image_details = {}

        images_info = {
            "bulb": ("bulb.png", (100, 100)),
            "thermostat": ("thermostat.png", (100, 100)),
            "cctv": ("cctv.png", (80, 80)),
            "oven": ("oven.png", (100, 100)),
            "fridge": ("fridge.png", (90, 100)),
            "chargingstation": ("chargingstation.png", (80, 90)),
        }

        for name, (filename, size) in images_info.items():
            image_path = os.path.join(image_folder, filename)  
            image_details[name] = fetch_image_from_local(image_path, size)
        
    #============================================================================================================================
    
        def get_command(dtype,obj):

            if (dtype == "bulb"):
                return lambda : self.Bulb_setting(obj)
            
            elif (dtype == "thermostat"):
                return lambda: self.Thermostat_settings(obj)
            
            elif (dtype == "cctv"):
                return lambda: self.CCTV_settings(obj)
            
            elif (dtype == "oven"):
                return lambda: self.Oven_settings(obj)
            
            elif (dtype == "fridge"):
                return lambda: self.Fridge_settings(obj)
            
            else:
                return lambda: self.ChargingStation_settings(obj)
        
    #============================================================================================================================

        def add_device_squares(parent ,image = image_details):

            i = 0
            set_temp = set(self.userobj.Section_list)
            self.userobj.Section_list = list(set_temp)
            print(self.userobj.Section_list)
            for secs in self.userobj.Section_list:
                print(secs)
                set_temp2 = set(secs.Device_list)
                secs.Device_list = list(set_temp2)
                print(secs.Device_list)
                for objs in secs.Device_list:  
                    dtype = objs.type
                    name = objs.name
                    final_image = image[dtype]

                    device_frame = ctk.CTkFrame(parent, width=200, height=250, corner_radius=15, fg_color="#2E3A46")
                    device_frame.grid(row=i // 3, column=i % 3, padx=20, pady=20)

                    image_placeholder = ctk.CTkLabel(device_frame, image = final_image , width=150, height=100, fg_color="#58677C", text = " " ,corner_radius=10)
                    image_placeholder.pack(pady=(15, 10))

                    device_name = ctk.CTkLabel(device_frame, text=name, font=("Arial", 14), text_color="white")
                    device_name.pack(pady=(5, 10))

                    command_fin = get_command(dtype,objs)

                    dots_button = ctk.CTkButton(device_frame, text="...", width=50, fg_color="#3F4E5C", text_color="white",command = command_fin)
                    dots_button.pack(pady=10)

                    i += 1

    #=============================================================================================================================================
        # Sidebar
        sidebar_frame = ctk.CTkFrame(app, width=150, corner_radius=0, fg_color="#2C2F33")
        sidebar_frame.pack(side="left", fill="y")
        
        all_devices_button = ctk.CTkButton(sidebar_frame, text="All Devices", width=120)
        all_devices_button.pack(pady=(20, 10), padx=10)

        filter_sections_button = ctk.CTkButton(sidebar_frame, text="Filter by Sections", width=120,command = self.filter_sections)
        filter_sections_button.pack(pady=10, padx=10)

        add_device_button = ctk.CTkButton(sidebar_frame, text="Add Device", width=120 ,command = self.add_device)
        add_device_button.pack(pady=10, padx=10)

        add_section_button = ctk.CTkButton(sidebar_frame, text="Add Sections", width=120,command = self.add_sections)
        add_section_button.pack(pady=10, padx=10)

        logout_button = ctk.CTkButton(sidebar_frame, text="Log Out", width=120, fg_color="red", text_color="white",command = self.Logout)
        logout_button.pack(side="bottom", pady=5, padx=10)

        Status_button = ctk.CTkButton(sidebar_frame, text="Status", width=120,command = self.Status_report)
        Status_button.pack(side = "bottom",pady = 20,padx = 10)

        main_frame = ctk.CTkFrame(app, corner_radius=10, fg_color="#a6a6a6")
        main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        canvas = Canvas(main_frame, bg="#D1D8C5", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        devices_frame = ctk.CTkFrame(canvas, fg_color="transparent")
        canvas.create_window((0, 0), window=devices_frame, anchor="nw")

        add_device_squares(devices_frame)

        devices_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))     

#==================================================================================================================================================

    def filtered_main_dashboard(self,section):

        app = self.app

        for widget in app.winfo_children():
            widget.destroy()
            
        app.minsize(760,600)
        app.maxsize(760,600)

        def fetch_image_from_local(path, size):
            """
            Fetches an image from the local filesystem, resizes it, and converts it to a CTkImage.
            
            Args:
                path (str): The path to the image file.
                size (tuple): The desired size of the image (width, height).

            Returns:
                CTkImage: Resized image suitable for use in CustomTkinter.
            """
            try:
                img = Image.open(path)  # Open the image from the local path
                img = img.resize(size)  # Resize the image
                return ctk.CTkImage(light_image=img, dark_image=img, size=size)  # Return a CTkImage
            except Exception as e:
                print(f"Error loading image from {path}: {e}")
                return None  # Return None if there's an error

        image_folder = "images"  
        image_details = {}

        images_info = {
            "bulb": ("bulb.png", (100, 100)),
            "thermostat": ("thermostat.png", (100, 100)),
            "cctv": ("cctv.png", (80, 80)),
            "oven": ("oven.png", (100, 100)),
            "fridge": ("fridge.png", (90, 100)),
            "chargingstation": ("chargingstation.png", (80, 90)),
        }

        for name, (filename, size) in images_info.items():
            image_path = os.path.join(image_folder, filename)  
            image_details[name] = fetch_image_from_local(image_path, size)
        
    #============================================================================================================================
    
        def get_command(dtype,obj):

            if (dtype == "bulb"):
                return lambda : self.Bulb_setting(obj)
            
            elif (dtype == "thermostat"):
                return lambda: self.Thermostat_settings(obj)
            
            elif (dtype == "cctv"):
                return lambda: self.CCTV_settings(obj)
            
            elif (dtype == "oven"):
                return lambda: self.Oven_settings(obj)
            
            elif (dtype == "fridge"):
                return lambda: self.Fridge_settings(obj)
            
            else:
                return lambda: self.ChargingStation_settings(obj)
        
    #============================================================================================================================

        def add_device_squares(parent ,image = image_details):

            i = 0
            set_temp = set(self.userobj.Section_list)
            self.userobj.Section_list = list(set_temp)
            print(self.userobj.Section_list)
            for secs in self.userobj.Section_list:
                if (secs.name==section):
                    print(secs)
                    set_temp2 = set(secs.Device_list)
                    secs.Device_list = list(set_temp2)
                    print(secs.Device_list)
                    for objs in secs.Device_list:  
                        dtype = objs.type
                        name = objs.name
                        final_image = image[dtype]

                        device_frame = ctk.CTkFrame(parent, width=200, height=250, corner_radius=15, fg_color="#2E3A46")
                        device_frame.grid(row=i // 3, column=i % 3, padx=20, pady=20)

                        image_placeholder = ctk.CTkLabel(device_frame, image = final_image , width=150, height=100, fg_color="#58677C", text = " " ,corner_radius=10)
                        image_placeholder.pack(pady=(15, 10))

                        device_name = ctk.CTkLabel(device_frame, text=name, font=("Arial", 14), text_color="white")
                        device_name.pack(pady=(5, 10))

                        command_fin = get_command(dtype,objs)

                        dots_button = ctk.CTkButton(device_frame, text="...", width=50, fg_color="#3F4E5C", text_color="white",command = command_fin)
                        dots_button.pack(pady=10)

                        i += 1

    #=============================================================================================================================================
        # Sidebar
        sidebar_frame = ctk.CTkFrame(app, width=150, corner_radius=0, fg_color="#2C2F33")
        sidebar_frame.pack(side="left", fill="y")
        
        all_devices_button = ctk.CTkButton(sidebar_frame, text="All Devices", width=120)
        all_devices_button.pack(pady=(20, 10), padx=10)

        filter_sections_button = ctk.CTkButton(sidebar_frame, text="Filter by Sections", width=120,command = self.filter_sections)
        filter_sections_button.pack(pady=10, padx=10)

        add_device_button = ctk.CTkButton(sidebar_frame, text="Add Device", width=120 ,command = self.add_device)
        add_device_button.pack(pady=10, padx=10)

        add_section_button = ctk.CTkButton(sidebar_frame, text="Add Sections", width=120,command = self.add_sections)
        add_section_button.pack(pady=10, padx=10)

        logout_button = ctk.CTkButton(sidebar_frame, text="Log Out", width=120, fg_color="red", text_color="white",command = self.Logout)
        logout_button.pack(side="bottom", pady=20, padx=10)

        Status_button = ctk.CTkButton(sidebar_frame, text="Status", width=120,command = self.Status_report)
        Status_button.pack(side = "bottom",pady = 20,padx = 10)

        main_frame = ctk.CTkFrame(app, corner_radius=10, fg_color="#a6a6a6")
        main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        canvas = Canvas(main_frame, bg="#D1D8C5", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        devices_frame = ctk.CTkFrame(canvas, fg_color="transparent")
        canvas.create_window((0, 0), window=devices_frame, anchor="nw")

        add_device_squares(devices_frame)

        devices_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))     

#==========================================================================================================================================================

    def Logout(self):
        self.show_home()

#=============================================================================================================================================

    def all_devices(self):
        for widget in self.app.winfo_children():
           widget.destroy()
        self.MainDashboard()

#============================================================================================================================================

    def add_device(self):
        root = ctk.CTk()
        root.title("Add Device")
        root.geometry("400x450")
        root.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        title_label = ctk.CTkLabel(root, text="Add Device", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        section_label = ctk.CTkLabel(root, text="Select a section of your house:", font=("Arial", 16))
        section_label.pack(pady=10)

        sections = []
        for secs in self.userobj.Section_list:
            sections.append(secs.name)
        selected_section = ctk.StringVar(value="Select a section")
        section_dropdown = ctk.CTkOptionMenu(root, values=sections, variable=selected_section)
        section_dropdown.pack(pady=10)

        device_label = ctk.CTkLabel(root, text="Select a device to add:", font=("Arial", 16))
        device_label.pack(pady=10)

        devices = ["bulb", "cctv", "thermostat", "oven", "fridge"]
        selected_device = ctk.StringVar(value="Select a device")
        device_dropdown = ctk.CTkOptionMenu(root, values=devices, variable=selected_device)
        device_dropdown.pack(pady=10)

        entry_label = ctk.CTkLabel(root, text="Enter Device Name:", font=("Arial", 14))
        entry_label.pack(pady=10)

        device_name_entry = ctk.CTkEntry(root, placeholder_text="Enter name")
        device_name_entry.pack(pady=10)

        def add_device_action():
            section = selected_section.get()
            device = selected_device.get()
            device_name = device_name_entry.get()
            
            if section == "Select a section" or device == "Select a device" or not device_name:
                print("Please fill out all fields!")
            else:
                device_obj = hm.HomeManager.addDevice(section,device_name,device)
                for secs in self.userobj.Section_list:
                    if (secs.name == section):
                        secs.Device_list.append(device_obj)
                        self.Device_details = csvh.CSV_Handler.loadDevices()
                        break
                self.House_details = csvh.CSV_Handler.loadHouses()
                for secs in self.House_details[self.userobj.username]["data"]:
                    if secs[0] == section:
                        temp_lst = [device_obj.device_id,device]
                        tup = tuple(temp_lst)
                        secs.append(tup)
                csvh.CSV_Handler.updateHouses(self.House_details)
                root.destroy()
                for widget in self.app.winfo_children():
                    widget.destroy()
                self.MainDashboard()

        add_button = ctk.CTkButton(root, text="Add", font=("Arial", 14), command=add_device_action)
        add_button.pack(pady=20)

        root.mainloop()

#===============================================================================================================================================

    def add_sections(self):

        root = ctk.CTk()
        root.title("Add Section")
        root.geometry("400x400")
        root.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        title_label = ctk.CTkLabel(root, text="Add Section", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        description_label = ctk.CTkLabel(root, text="Select a section of your house", font=("Arial", 16))
        description_label.pack(pady=10)

        sections = ["Bedroom", "Bathroom", "LivingRoom", "Garage", "Kitchen"]
        selected_section = ctk.StringVar(value="Choose a section")
        dropdown = ctk.CTkOptionMenu(root, values=sections ,variable=selected_section)
        dropdown.pack(pady=10)

        entry_label = ctk.CTkLabel(root, text="Enter Section Name:", font=("Arial", 14))
        entry_label.pack(pady=10)

        section_name_entry = ctk.CTkEntry(root, placeholder_text="Enter name")
        section_name_entry.pack(pady=10)

        def add_func(root,section_type,sectionname):
            if (section_type != "Select"):
                section_obj = self.userobj.add_section(sectionname,section_type)
                self.userobj.Section_list.append(section_obj)
            root.destroy()

        
        add_button = ctk.CTkButton(root, text="Add", font=("Arial", 14), command=lambda: add_func(root,dropdown.get(),section_name_entry.get()))
        add_button.pack(pady=20)

        root.mainloop()

#==========================================================================================================================================================

    def filter_sections(self):
        root = ctk.CTk()
        root.title("Filter By Sections")
        root.geometry("400x300")
        root.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        title_label = ctk.CTkLabel(root, text="Select Section", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        description_label = ctk.CTkLabel(root, text="Select a section of your house", font=("Arial", 16))
        description_label.pack(pady=10)

        sections = []
        for secs in self.userobj.Section_list:
            sections.append(secs.name)
        selected_section = ctk.StringVar(value="Choose a section")
        dropdown = ctk.CTkOptionMenu(root, values=sections , variable = selected_section)
        dropdown.pack(pady=10)

        def filter_func(root,section):
            print(section)
            print(section)
            print(section)
            
            root.destroy()
            for widget in self.app.winfo_children():
                widget.destroy()
            self.filtered_main_dashboard(section)

        filter_button = ctk.CTkButton(root, text="Filter", font=("Arial", 14), command=lambda: filter_func(root,dropdown.get()))
        filter_button.pack(pady=20)

        root.mainloop()

#==========================================================================================================================================
    
    def Status_report(self):
        app = ctk.CTk()
        app.title("Status Report")
        app.geometry("300x300")

        ctk.set_appearance_mode("light") 
        ctk.set_default_color_theme("blue")  

        title_label = ctk.CTkLabel(
            app, text="Status Report", font=("Arial", 24, "bold"), text_color="black"
        )
        title_label.pack(pady=(40, 10))

        subtitle_label = ctk.CTkLabel(
            app,
            text="Select a Section to View its Status",
            font=("Arial", 14),
            text_color="gray",
        )
        subtitle_label.pack(pady=(0, 20))

        sections = ["cctv", "bulb", "thermostat", "fridge", "oven"]
        section_label = ctk.CTkLabel(app, text="Select Device:", font=("Arial", 16))
        section_label.pack(pady=(10, 5))

        section_dropdown = ctk.CTkOptionMenu(app, values=sections)
        section_dropdown.pack(pady=(5, 20))
        section_dropdown.set("Select Device") 

        def generate_report():
            selected_device = section_dropdown.get()
            if selected_device != "Select Device":
                st.StatusReport(selected_device,self.userobj.Section_list)
            else:
                ctk.CTkMessagebox(
                    title="Error",
                    message="Please select a Device before generating the report!",
                    icon="warning",
                )

        report_button = ctk.CTkButton(app,text="Report",command=generate_report,text_color="white",fg_color="#0078D7",font=("Arial", 16))
        report_button.pack(pady=(10, 30))

        app.mainloop()

#=================================================================================================================================================================

    def delete_device(self):
        pass

#============================================================================================================================================   
# app = ctk.CTk()
# app.geometry("400x300")
# app.title("Home Management System")
# app.configure(bg="#f4f5f7")

# GUIObj = GUI(app,Member_details,House_details,Device_Details)
# GUIObj.show_home()

# app.mainloop()


