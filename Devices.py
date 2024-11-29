import uuid  # for unique id
from datetime import datetime


class Device:
    device_details = {}

    def __init__(self, name, device_type):
        self.name = name
        self.device_id = str(uuid.uuid4())
        self.type = device_type
        self.status = "on"
        self.automation_rules = []  # Initialize the automation rules

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

    def updateStatus(self, status):
        self.status = status

    def updateBrightness(self, update):
        self.Brightness = update

    def updateWarmth(self, update):
        self.Warmth = update

    def updateColour(self, update):
        self.Colour = update

    def set_automation(self):
        # Example Rule: Turn on the bulb at 6:00 PM
        def condition():
            return datetime.now().hour == 18  # Check if it's 6:00 PM

        def action():
            self.updateStatus("on")
            print(f"{self.name}: Bulb is now ON.")

        self.add_automation_rule(condition, action)


class Security_camera(Device):
    def __init__(self, name):
        super().__init__(name, "security_camera")
        self.Resolution = "FHD"  # Resolution options: [SD, HD, FHD]
        self.Mode = "day"  # Mode options: ['day', 'night']

    def updateStatus(self, status):
        self.status = status

    def updateResolution(self, update):
        self.Resolution = update

    def updateMode(self, update):
        self.Mode = update

    def set_automation(self):
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
        self.Mode = "cool"  # Thermo mode options: [Heat, Cool, Fan]

    def updateStatus(self, status):
        self.status = status

    def updateTemperature(self, update):
        self.Temperature = update

    def updateMode(self, update):
        self.Mode = update

    def set_automation(self):
        # Rule: Adjust thermostat temperature based on outside temperature
        def condition():
            outside_temperature = 35  # Example hardcoded outside temperature
            return outside_temperature > 30  # Trigger if outside temperature > 30°C

        def action():
            self.updateTemperature(22)  # Set thermostat temperature to 22°C
            print(f"{self.name}: Thermostat temperature set to 22°C.")

        self.add_automation_rule(condition, action)


class Garagedoor(Device):
    def __init__(self, name):
        super().__init__(name, "garagedoor")
        self.lock = "enable"  # Lock settings: ['enable', 'disable']
        self.doorspeed = "normal"  # Door speed options: ['fast', 'normal', 'slow']

    def updateStatus(self, status):
        self.status = status

    def updateLock(self, update):
        self.lock = update

    def updateDoorspeed(self, update):
        self.doorspeed = update

    def set_automation(self):
        # Rule: Open the garage door at 9 AM and 5 PM
        def condition():
            current_hour = datetime.now().hour
            return current_hour == 9 or current_hour == 17  # 9 AM or 5 PM

        def action():
            self.updateStatus("open")  # Open the garage door
            print(f"{self.name}: Garage door is now OPEN.")

        self.add_automation_rule(condition, action)


class Oven(Device):
    def __init__(self,name):
        super().__init__(name, "oven")
                #attributes
        self.mode="bake"                    # modes are['bake', 'broil', 'roast', 'toast']
        self.temperature=100                       #temp should be an integer between 50-300 degrees celsius
        self.cooktime=2                     #don't know if we should add this but if we do we need interval from 1 minute - 12 hours
            
    def updateStatus(self, status):
        self.status = status
    
    def updateCooktime(self,time):
        self.cooktime=time
    
    def updateTemperature(self , update):
        self.Temperature = update
    
    def updateMode(self , update):
        self.mode = update

    def set_automation(self):
        # Rule: Notify when cooking is finished
        def condition():
            return self.status == "off" and self.cooktime >= 0  # If oven is off and cooking time passed

        def action():
            print(f"{self.name}: Cooking is done! You can now take your food out.")
            # You can add an actual notification here if needed.

        self.add_automation_rule(condition, action)

#automation

class Refrigerator(Device):
    def __init__(self, name):
        super().__init__(name, "refrigerator")

    def update_status(self, status):
        """Updates the status of the refrigerator."""
        self.status = status


class Fridge(Refrigerator):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 3  # Default fridge temperature: 3°C
        self.humidity = "high"  # Default humidity: high

    def update_temperature(self, temp):
        """Updates the fridge temperature."""
        self.temperature = temp

    def update_humidity(self, humidity):
        """Updates the humidity setting of the fridge."""
        self.humidity = humidity

    def set_automation(self):
        # Example Rule: Lower humidity at 6 PM
        def condition():
            return datetime.now().hour == 18  # Trigger at 6 PM

        def action():
            self.update_humidity("low")
            print(f"{self.name}: Fridge humidity set to LOW.")

        self.add_automation_rule(condition, action)


class Freezer(Refrigerator):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = -18  # Default freezer temperature: -18°C

    def update_temperature(self, temp):
        """Updates the freezer temperature."""
        self.temperature = temp

    def set_automation(self):
        # Example Rule: Reduce temperature at 10 PM
        def condition():
            return datetime.now().hour == 22  # Trigger at 10 PM

        def action():
            self.update_temperature(-20)  # Reduce freezer temperature
            print(f"{self.name}: Freezer temperature set to -20°C.")

        self.add_automation_rule(condition, action)


class Charging_hub(Device):
    def __init__(self,name,number_of_ports,maxwattage):
        super().__init__(name,'Charging_hub')
        self.numberofports=number_of_ports
        self.maxwattage=maxwattage                          #max power the hub can supply at once                              
        self.connecteddevices=[]
        self.wattageused=0                                 #power currently being supplied by hub

    numconnecteddevices=0
    
    def connect_dev(self,dev_name,powerdrawnbydev):
        if numconnecteddevices<=self.numberofports and self.wattageused+powerdrawnbydev<=self.maxwattage:
            numconnecteddevices+=1
            self.connecteddevices.append(dev_name)
            self.wattageused+=powerdrawnbydev
            self.updateStatus()

        else:
            pass        #have to print no more ports left or something
    
    def updateStatus(self):
        if self.wattageused>0:
            self.status='on'
        elif self.wattageused==0:
            self.status='off'

    def set_automation(self):
            # Example Rule: Turn off charging hub if no devices are connected
            def condition():
                return len(self.connected_devices) == 0
    
            def action():
                self.status = "off"
                print(f"{self.name}: Charging Hub turned OFF.")
    
            self.add_automation_rule(condition, action)


'''
# Test cases
if __name__ == "__main__":
    # Create device instances
    bulb = Bulb("Living Room Bulb")
    camera = Security_camera("Front Door Camera")
    thermostat = Thermostat("Home Thermostat")
    garage = Garagedoor("Main Garage Door")

    # Set automation rules
    bulb.set_automation()
    camera.set_automation()
    thermostat.set_automation()
    garage.set_automation()

    # Apply automation rules (Simulate at specific times)
    print("\n--- Testing Automation Rules ---")
    bulb.apply_rules()
    camera.apply_rules()
    thermostat.apply_rules()
    garage.apply_rules()

    # Status reports
    print("\n--- Device Status Reports ---")
    print(bulb.status_report())
    print(camera.status_report())
    print(thermostat.status_report())
    print(garage.status_report())
'''




