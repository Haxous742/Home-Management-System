import CSV_Handler as csvh
import uuid  
from datetime import datetime


class Device:

    device_details =  csvh.CSV_Handler.loadDevices()
    #format = {"device_id" : {"name" : <> , "type" : <>, "status" : <> , "attributes" :{"attribute1" : "status","attribute2":"status"}}}


    def __init__(self, name, device_type):
        self.name = name
        self.device_id = str(uuid.uuid4())
        self.type = device_type
        self.status = "off"
        self.automation_rules = []  

    def status_report(self):
        return {
            "name": self.name,
            "device_id": self.device_id,
            "type": self.type,
            "status": self.status,
        }

    def add_automation_rule(self, condition, action):
        """Adds a new automation rule with a condition and action."""
        self.automation_rules.append({"condition": condition, "action": action})

    def apply_rules(self):
        """Evaluates and applies all automation rules."""
        for rule in self.automation_rules:
            if rule["condition"]():
                rule["action"]()


class Bulb(Device):
    def __init__(self, name):
        super().__init__(name, "bulb")
        self.Brightness = 50  #1-100
        self.Warmth =  50 # Warmth options: 1-100
        self.Colour = 50 # Colour options: 1-100
        Device.device_details =  csvh.CSV_Handler.loadDevices()

    def update_id(self,id):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.device_id = id

    def updateStatus(self, status):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.status = status
        Device.device_details[self.device_id]['status'] = status
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateBrightness(self, update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.Brightness = update
        Device.device_details[self.device_id]['attributes']['Brightness'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateWarmth(self, update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.Warmth = update
        Device.device_details[self.device_id]['attributes']['Warmth'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateColour(self, update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()    
        self.Colour = update
        Device.device_details[self.device_id]['attributes']['Colour'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateName(self,name):
        Device.device_details =  csvh.CSV_Handler.loadDevices()      
        self.name = name
        Device.device_details[self.device_id]['name']= name 
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def set_automation(self):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        # Example Rule: Turn on the bulb at 6:00 PM
        def condition():
            return datetime.now().hour == 18  # Check if it's 6:00 PM

        def action():
            self.updateStatus("on")
            print(f"{self.name}: Bulb is now ON.")

        self.add_automation_rule(condition, action)


class Security_camera(Device):
    def __init__(self, name):
        super().__init__(name, "cctv")
        self.Resolution = "720"  # Resolution options: ["720p", "1080p", "4K", "8K"]
        self.Mode = "Day"  # Mode options: ['day', 'night']
        Device.device_details =  csvh.CSV_Handler.loadDevices()

    def update_id(self,id):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.device_id = id        

    def updateStatus(self, status):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.status = status
        Device.device_details[self.device_id]['status'] = status
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateResolution(self, update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.Resolution = update
        Device.device_details[self.device_id]['attributes']['Resolution'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)
        

    def updateMode(self, update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.Mode = update
        Device.device_details[self.device_id]['attributes']['Mode'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateName(self,name):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.name = name
        Device.device_details[self.device_id]['name']= name 
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def set_automation(self):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        # Rule: Change to night mode after 9 PM
        def condition():
            return datetime.now().hour >= 21  # After 9 PM

        def action():
            self.updateMode("night")
            self.updateResolution("HD")
            print(f"{self.name}: Security Camera is now in NIGHT mode.")

        self.add_automation_rule(condition, action)


class Thermostat(Device):
    def __init__(self, name):
        super().__init__(name, "thermostat")
        self.Temperature = 24  # Temperature settings: [int between 16 to 40]
        self.Mode = "Cool"  # Thermo mode options: [Heat, Cool, Fan]
        Device.device_details =  csvh.CSV_Handler.loadDevices()        

    def update_id(self,id):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.device_id = id

    def updateStatus(self, status):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.status = status
        Device.device_details[self.device_id]['status'] = status
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateTemperature(self, update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.Temperature = update
        Device.device_details[self.device_id]['attributes']['Temperature'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateMode(self, update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.Mode = update
        Device.device_details[self.device_id]['attributes']['Mode'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateName(self,name):
        Device.device_details =  csvh.CSV_Handler.loadDevices()        
        self.name = name
        Device.device_details[self.device_id]['name']= name 
        csvh.CSV_Handler.updateDevices(Device.device_details)


    def set_automation(self):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        # Rule: Adjust thermostat temperature based on outside temperature
        def condition():
            outside_temperature = 35  # Example hardcoded outside temperature
            return outside_temperature > 30  # Trigger if outside temperature > 30°C

        def action():
            self.updateTemperature(22)  # Set thermostat temperature to 22°C
            print(f"{self.name}: Thermostat temperature set to 22°C.")

        self.add_automation_rule(condition, action)


class Oven(Device):
    def __init__(self,name):
        super().__init__(name, "oven")
                #attributes
        self.mode="Bake"                    # modes are ["Preheat", "Boil", "Bake", "Air Fry","Defrost"]
        self.temperature=100                       #temp should be an integer between 50-300 degrees celsius
        self.cooktime=2                     #don't know if we should add this but if we do we need interval from 1 minute - 12 hours
        Device.device_details =  csvh.CSV_Handler.loadDevices()

    def update_id(self,id):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.device_id = id

    def updateStatus(self, status):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.status = status
        Device.device_details[self.device_id]['status'] = status
        csvh.CSV_Handler.updateDevices(Device.device_details)
        
    
    def updateCooktime(self,time):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.cooktime=time
        Device.device_details[self.device_id]['attributes']['Cooktime'] = time
        csvh.CSV_Handler.updateDevices(Device.device_details)
    
    def updateTemperature(self , update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.temperature = update
        Device.device_details[self.device_id]['attributes']['Temperature'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateMode(self , update):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.mode = update
        Device.device_details[self.device_id]['attributes']['Mode'] = update
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def updateName(self,name):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.name = name
        Device.device_details[self.device_id]['name'] = name 
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def set_automation(self):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        # Rule: Notify when cooking is finished
        def condition():
            return self.status == "off" and self.cooktime >= 0  # If oven is off and cooking time passed

        def action():
            print(f"{self.name}: Cooking is done! You can now take your food out.")
            # You can add an actual notification here if needed.

        self.add_automation_rule(condition, action)


class Refrigerator(Device):

    def __init__(self, name):
        super().__init__(name, "fridge")
        Device.device_details =  csvh.CSV_Handler.loadDevices()

    def make_objs(self):
        self.Fridgeobj = Fridge(self.device_id)
        self.Freezerobj = Freezer(self.device_id)

    def update_id(self,id):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.device_id = id

    def updateStatus(self, status):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        """Updates the status of the refrigerator."""
        self.status = status
        Device.device_details[self.device_id]['status'] = status
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def update_name(self,name):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        self.name = name
        Device.device_details[self.device_id]['name'] = name 
        csvh.CSV_Handler.updateDevices(Device.device_details)


class Fridge(Refrigerator):
    def __init__(self,id):
        self.temperature = 3  # Default fridge temperature: 3°C
        self.humidity = "High"  # Default humidity: high , medium , low
        self.id = id
        Device.device_details =  csvh.CSV_Handler.loadDevices()

    def update_temperature(self, temp):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        """Updates the fridge temperature."""
        self.temperature = temp
        Device.device_details[self.id]['attributes']['Fridge_Temperature'] = temp
        csvh.CSV_Handler.updateDevices(Device.device_details)
 

    def update_humidity(self, humidity):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        """Updates the humidity setting of the fridge."""
        self.humidity = humidity
        Device.device_details[self.id]['attributes']['Fridge_humidity'] = humidity
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def set_automation(self):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        # Example Rule: Lower humidity at 6 PM
        def condition():
            return datetime.now().hour == 18  # Trigger at 6 PM

        def action():
            self.update_humidity("low")
            print(f"{self.name}: Fridge humidity set to LOW.")

        self.add_automation_rule(condition, action)


class Freezer(Refrigerator):

    def __init__(self,id):
        self.temperature = -18  # Default freezer temperature: -18°C
        self.id = id
        Device.device_details =  csvh.CSV_Handler.loadDevices()

    def update_temperature(self, temp):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        """Updates the freezer temperature."""
        self.temperature = temp
        Device.device_details[self.id]['attributes']['Freezer_Temperature'] = temp
        csvh.CSV_Handler.updateDevices(Device.device_details)

    def set_automation(self):
        Device.device_details =  csvh.CSV_Handler.loadDevices()
        # Example Rule: Reduce temperature at 10 PM
        def condition():
            return datetime.now().hour == 22  # Trigger at 10 PM

        def action():
            self.update_temperature(-20)  # Reduce freezer temperature
            print(f"{self.name}: Freezer temperature set to -20°C.")

        self.add_automation_rule(condition, action)
