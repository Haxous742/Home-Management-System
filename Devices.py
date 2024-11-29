import CSV_Handler as csvh
import uuid                 #for unique id

class Device:

    device_details = {}
     #format = {"device_id" : {"name" : <> , "type" : <>, "status" : <> , "attributes" :{"attribute1" : "status","attribute2":"status"}}}

    def __init__(self , name , device_type ):
        self.name = name
        self.device_id = str(uuid.uuid4())
        self.type = device_type
        self.status = "on"
        self.attributes = {}

    def status_report(self):
        pass
        


class Bulb(Device):

    def __init__(self ,name):
        super().__init__(name,"bulb")

        #attributes
        self.Brightness = 0
        self.Warmth = "Low"             #warmth options : [Low , Medium , High]
        self.Colour = "White"           #colour options : [White , Yellow , red , green ,blue]

    def updateStatus(self, status):
        self.status = status
    
    def updateBrightness(self , update):
        self.Brightness = update
    
    def updateWarmth(self , update):
        self.Warmth = update

    def updateColour(self , update):
        self.Colour = update

    #write preset func here (turns on automatically at a certain time)


class Security_camera(Device):

    def __init__(self,name):
        super().__init__(name,"security_camera")

    #attributes

        self.Resolution = 'FHD'         #reolution options : [SD , HD , FHD]
        self.RecordingStatus = ""       #RecordingStatus opts : []


    def updateStatus(self, status):
        self.status = status
    
    def updateResolution(self , update):
        self.Resolution = update
    
    def updateRecordingStatus(self , update):
        self.RecordingStatus = update

    #write preset func here (automaticallly  turn on recording at a certain time)



class Thermostat(Device):

    def __init__(self,name):
        super().__init__(name,"thermostat")

    #attributes

        self.Temperature =  24         #temperature settings : [int bw 16 to 30]
        self.Mode = "cool"                 #thermo mode opts : [Heat , cool ,fan]


    def updateStatus(self, status):
        self.status = status
    
    def updateTemperature(self , update):
        self.Temperature = update
    
    def updateMode(self , update):
        self.Mode = update

    #write preset func here



class Garagedoor(Device):

    def __init__(self,name):
        super().__init__(name,"garagedoor")

    #attributes

        self.lock = 'enable'               #lock settings:[enable , disable`]
        self.doorspeed =  'normal'               #garagedoor mode opts : ['fast' , 'normal' ,'slow']


    def updateStatus(self, status):
        self.status = status
    
    def updateLock(self , update):
        self.lock = update
    
    def updateDoorspeed(self , update):
        self.doorspeed = update

    #write preset func here



