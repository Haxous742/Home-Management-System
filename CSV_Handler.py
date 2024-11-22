import csv 

class CSV_Handler:

    #Class Members
    #nested Dictionary 
    #formal of Dict = {'Username' : {'Password' : <> , 'Address' : <> , 'Houses' : ['House_1' , 'House_2'] } }

    @staticmethod
    def loadMembers():
        dict = {}
        with open('Members.csv',mode = 'r') as file:
            reader = csv.reader(file)
            for row in reader:  #format of row in CSV file: Username,Password,Address,House_1%House_2... (seperated by %) 
                dict[row[0]] = {'Password':row[1] ,'Address':row[2] ,'Houses': row[3].strip().split("%") }

        return dict
    
    @staticmethod
    def updateMembers(dict):
        with open('Members.csv',mode ='w', newline='') as file:
            writer = csv.writer(file)
            for key in dict.keys():
                Houses = ''
                for val in dict[key]['Houses']:
                    Houses+=val +"%"
                row = [key,dict[key]['Password'],dict[key]['Address'],Houses]
                writer.writerow(row)

#========================================================================================================================================
    #Class Devices
    #nested dictionary
    #format = {"device_id" : {"name" : <> , "type" : <>, "status" : <> , "attributes" :{"attribute1" : "status","attribute2":"status"}}}

    @staticmethod
    def loadDevices():
        with open("Devices.csv",mode = 'r') as file:
            dict = {}
            reader = csv.reader(file)
            for row in reader:  #Formal for CSV file : device_id,name,type,status,attribute1_status,attribute2_status ....
                dict_temp = {}
                for i in range(4,len(row)):
                    temp = row[i].strip().split("_")
                    dict_temp[temp[0]] = temp[1]

                dict[row[0]] = {"name" : row[1],"type" : row[2], "status" : row[3], "attributes" : dict_temp}

            return dict
        
    @staticmethod
    def updateDevices(dict):
        with open("Devices.csv", mode = 'w', newline='') as file:
            writer = csv.writer(file)
            for key in dict.keys():
                row = [key,dict[key]["name"],dict[key]["type"],dict[key]["status"]]
                for keys in dict[key]["attributes"]:
                    str_temp = f'{keys}_{dict[key]["attributes"][keys]}'
                    row.append(str_temp)
                writer.writerow(row)

#===================================================================================================================
    #Class Houses
    #nested dictionaries
    #format = {"House_ID":{"Name" : <name> , "data" : <data>}}
        #format of <data> (nested lists):
        #       [["section1_name","device1_Id","device2_id"....],["section2_name","device1_Id"."device2_Id"....]....]    
                
    @staticmethod
    def loadHouses():
        with open("Houses.csv",mode = 'r') as file:
            dict = {}
            reader = csv.reader(file)
            for row in reader:  #format of csv_file : House_Id,Name,<Section1_name>_<Device1_Id>_<Device2_Id>,<Section2_name>_<Device1_Id>_<Device2_Id>,....
                data = []
                for i in range(2,len(row)):
                    lst_temp = []
                    lst_temp = row[i].strip().split("_")
                    data.append(lst_temp)
                dict[row[0]] = {"Name" : row[1],"Data" : data}

        return dict
            
    @staticmethod
    def updateHouses(dict):
        with open("Houses.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            for key in dict.keys():
                row = [key,dict[key]["name"]]
                for val in dict[key]["data"]:
                    str_temp = val[0]
                    for i in range(1,len(val)):
                        str_temp = str_temp + f"_{val[i]}"
                    row.append(str_temp)
                writer.writerow(row)
                
#==========================================================================================================================================
