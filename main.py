import tkinter as tk
from UI_ctk import *
from CSV_Handler import CSV_Handler
from Members import *
from Houses import *
from Devices import *

root = ctk.CTk()
root.title("Home Management System")
root.geometry("400x300")
root.configure(bg="#f4f5f7")


Device_details = CSV_Handler.loadDevices()

Member_details = CSV_Handler.loadMembers()

House_details = CSV_Handler.loadHouses()

GuiObj = GUI(root,Member_details,House_details,Device_details)

GuiObj.show_home()

root.mainloop()
