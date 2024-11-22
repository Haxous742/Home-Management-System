import tkinter as tk
from UI import *
from CSV_Handler import CSV_Handler
from Members import *
from Houses import *
from Devices import *

root = tk.Tk()
root.title("Home Management System")
root.geometry("500x300")
root.config(bg="#f5f5f5")

DeviceObjs = Devices()
Devices.Device_details = CSV_Handler.loadDevices()

MemberObjs = Members()
Members.Member_details = CSV_Handler.loadMembers()

HouseObjs = Houses()
Houses.House_details = CSV_Handler.loadHouses()

GuiObj = GUI(root,MemberObjs,DeviceObjs,HouseObjs)

GuiObj.login_page()

root.mainloop()
