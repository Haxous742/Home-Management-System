import Houses as Houses
import Devices as Devices
import CSV_Handler as csvh

class HomeManager:

    device_typedict = {'bulb': [Devices.Bulb , {"Brightness" : 50 ,"Warmth": 50 , "Colour":50}] , 'cctv' : [Devices.Security_camera ,{"Resolution" : 720 ,"Mode": 'Day'}],'thermostat': [Devices.Thermostat,{"Temperature" : 24 ,"Mode": 'Cool'}] ,'oven': [Devices.Oven,{"Cooktime" : 2 ,"Temperature": 100 , "Mode":'Bake'}],'fridge':[ Devices.Refrigerator,{"Fridge_Temperature" : 3 ,"Fridge_humidity": 'High' }] }
    device_details =  csvh.CSV_Handler.loadDevices()
    #format = {"device_id" : {"name" : <> , "type" : <>, "status" : <> , "attributes" :{"attribute1" : "status","attribute2":"status"}}}

    @staticmethod
    def addDevice(section_name , device_name , device_type ):
        device_class = HomeManager.device_typedict[device_type][0]
        deviceobj = device_class(device_name)
        HomeManager.device_details[deviceobj.device_id] = {'name': deviceobj.name , 'type' :deviceobj.type, "status" : deviceobj.status , "attributes" : HomeManager.device_typedict[device_type][1] }
        print(HomeManager.device_details)
        csvh.CSV_Handler.updateDevices(HomeManager.device_details)

        return deviceobj

    @staticmethod
    def removeDevice(device_id):
        HomeManager.device_details.pop(device_id)
        csvh.CSV_Handler.updateDevices(HomeManager.device_details)
        
        
