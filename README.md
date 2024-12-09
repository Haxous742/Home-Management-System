# Python_Project-Team-22

------------------------------------------------------------------------------------------------------------------------------------------

**Project Home Automation system**

A home automation system that allows users to add and control various devices in their homes. They can automate their devices and generate system report for the devices. You can also add different section in a house .

------------------------------------------------------------------------------------------------------------------------------------------


**Commands to start the application**

1. Ensure Python 3.x is installed.
2. Run main.py using the following command :
   ```
   python main.py

------------------------------------------------------------------------------------------------------------------------------------------

**Supported Operating systems**

1. Windows
2. MacOs (Some commands might be different)
3. Linux

-----------------------------------------------------------------------------------------------------------------------------------------

**Prerequisites and Installation Steps**

We have install the following libraries :
1. customtkinter (need to be installed)
2. Pillow (need to be installed)
3. requests (need to be installed)


```
pip install customtkinter
pip install Pillow
pip install requests
```

-----------------------------------------------------------------------------------------------------------------------------------------

**Features Implemented**

1. Login and signup Page : A secure interface for users to create accounts and log in to the system.
    <img width="414" alt="Screenshot 2024-12-09 at 10 24 51 AM" src="https://github.com/user-attachments/assets/b3885820-5bce-405a-8273-1c2c125b8e27">
<img width="402" alt="Screenshot 2024-12-09 at 10 24 31 AM" src="https://github.com/user-attachments/assets/fd15d10b-deae-4372-83cb-48e491bfba33">


2. Add Sections : Users can create and manage different sections of a house, such as bedrooms or Living room.<img width="408" alt="Screenshot 2024-12-09 at 10 25 16 AM" src="https://github.com/user-attachments/assets/28a31f05-2f5d-4e25-abce-365ba6af18a4">
   
3. Add Devices : New Devices like bulb , cctv , thermostat, etc can be added to specific sections. <img width="400" alt="Screenshot 2024-12-09 at 10 25 48 AM" src="https://github.com/user-attachments/assets/ae426d53-2c3c-4a7b-a6cf-7ef86a18d3fb"><img width="772" alt="Screenshot 2024-12-09 at 11 09 04 AM" src="https://github.com/user-attachments/assets/48b1dbb8-7360-493b-909c-29adea819d0a">


4. View Device Settings : Access and modify the settings of each individual device from the home page. <img width="515" alt="Screenshot 2024-12-09 at 10 26 48 AM" src="https://github.com/user-attachments/assets/8da24056-c7b1-4338-b136-a2d654f8b4c1">
<img width="513" alt="Screenshot 2024-12-09 at 10 26 18 AM" src="https://github.com/user-attachments/assets/b4bbba05-0da8-4ec6-b61c-5b9d17ac7ed6">


5. Filter Devices by Section : Easily filter and view devices based on the section they belong to for quick navigation.
   <img width="403" alt="Screenshot 2024-12-09 at 11 09 54 AM" src="https://github.com/user-attachments/assets/c2a479bd-76c7-464d-98cd-8be8cc53746b">


7. Generate System Reports : Generate detailed system reports in .txt format for a particular device type, providing comprehensive insights.
<img width="1084" alt="Screenshot 2024-12-09 at 11 09 37 AM" src="https://github.com/user-attachments/assets/b000b97d-eb01-4c05-a46d-a5186a83afb1">


-----------------------------------------------------------------------------------------------------------------------------------------

**Libraries used**

1. customtkinter 
2. tkinter
3. csv
4. Pillow 
5. requests 
6. io
7. colorsys
-----------------------------------------------------------------------------------------------------------------------------------------

**Classes and Modules made**

1.Members: This class handles the login and sign-up functionality for users.

2.Deivce : A class designed to manage various devices. It includes multiple device types as subclasses, enabling users to update their attributes efficiently.
   
3.Houses: This class is responsible for managing different sections of a house. It includes device types as subclasses, allowing users to organize and update their attributes.

5. Csv Handler : A module dedicated to managing all CSV files, including Houses.csv, Members.csv, and Devices.csv.
   
6. UI : This module oversees the graphical user interface (GUI) of the application, ensuring a seamless user experience.

7. Homemanager : A module focused on functionality for adding and removing devices from specific sections within the house.

8. Status Report : A module that generates detailed .txt status reports for specific device types, providing insights into their attributes and current state.
-----------------------------------------------------------------------------------------------------------------------------------------


The Team
--------

|          Name                 | Roll Number |       Role                    |
|-------------------------------|-------------|-------------------------------|
| Vedant Mundada                | BT2024268   | GUI                           |
| Saarthak Singh                | IMT2024082  | Device class and system report|
| Ravva Sai Sujay               | IMT2024086  | Login and singup page         |
| Saanvi Choudhary              | BT2024223   | Houses class                  |
| Kaushiksai Yakkala            | BT2024240   | Devices subclass              |






