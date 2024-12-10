import CSV_Handler as csvh
import csv

# House_details = {
#             "Vedant" : {"data" : [["Bedroom01","Bedroom",("B01","bulb"),("T01","thermostat"),("F01","fridge")],["Garage01","Garage",("T02","thermostat"),("O01","oven"),("C01","cctv")]]}
#             }

class Houses:

    filname = "Houses.csv"
    House_details = csvh.CSV_Handler.loadHouses()
    Section_list = []

    def Username_update(self,name):
        self.username = name

    def add_section(self,section_name,section_type):
        try:

            Houses.House_details = csvh.CSV_Handler.loadHouses()

            for keys in Houses.House_details.keys():
                if (keys == self.username):
                    lst_tmp = [section_name,section_type]
                    Houses.House_details[keys]["data"].append(lst_tmp)

                    if section_type == "Bedroom":
                        temp_obj = Bedroom(section_name)

                    elif section_type == "Kitchen":
                        temp_obj = Kitchen(section_name)

                    elif section_type == "Garage":
                        temp_obj = Garage(section_name)

                    elif section_name == "LivingRoom":
                        temp_obj = LivingRoom(section_name)

                    else:
                        temp_obj = Bathroom(section_name)
                    print("BEFORE+========================================")
                    print(Houses.House_details)
                    csvh.CSV_Handler.updateHouses(Houses.House_details)

            return temp_obj
        except Exception as e:
            return f"Error while adding section: {e}"

    def remove_section(self,section_name):
        try:
           for keys in self.House_details.keys():     
               if (keys == self.username):
                   for secs in self.House_details[keys]["data"]:
                       if secs[0]==section_name:
                           self.House_details[keys]["data"].remove(secs)
        except FileNotFoundError:
            return "Error: File not found. Please check the file path."
        except Exception as e:
            return f"Error while removing section: {e}"

    def update_section(self, house_id, section_name, new_section_name=None, *new_device_ids):
        try:
            updated_rows = []
            section_updated = False

            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == house_id and row[1] == section_name:
                        section_updated = True
                        updated_rows.append([house_id, new_section_name or section_name, *new_device_ids])
                    else:
                        updated_rows.append(row)

            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if section_updated:
                return f"Section '{section_name}' updated in house {house_id}."
            return f"Section '{section_name}' not found in house {house_id}."
        except FileNotFoundError:
            return "Error: File not found. Please check the file path."
        except Exception as e:
            return f"Error while updating section: {e}"
        
class Bedroom(Houses):

    def __init__(self,name):
        self.Type = "Bedroom"
        self.name = name

    Device_list = []

    def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Bedroom", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Bedroom", device_id)


class Kitchen(Houses):

    def __init__(self,name):
        self.Type = "Kitchen"
        self.name = name

    Device_list = []

    def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Kitchen", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Kitchen", device_id)


class Garage(Houses):

    def __init__(self,name):
        self.Type = "Garage"
        self.name = name
   
    Device_list = []

    def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Garage", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Garage", device_id)


class LivingRoom(Houses):

    def __init__(self,name):
        self.Type = "LivingRoom"
        self.name = name

    Device_list = []

    def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Living Room", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Living Room", device_id)


class Bathroom(Houses):

    def __init__(self,name):
        self.Type = "Bathroom"
        self.name = name
   
    Device_list = []
   
    def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Bathroom", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Bathroom", device_id)
