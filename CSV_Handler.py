import csv 

class CSV_Handler:

    #Class Members
    #nested Dictionary 
    #formal of Dict = {'Username' : {'Password' : <> , 'Address' : <> } }

    @staticmethod
    def loadMembers():
        dict = {}
        with open('Members.csv',mode = 'r',newline= "") as file:
            reader = csv.reader(file)
            for row in reader:  #format of row in CSV file: Username,Password,Address 
                dict[row[0]] = {'Password':row[1] ,'Address':row[2] }

        return dict
    
    @staticmethod
    def updateMembers(dict):
        with open('Members.csv',mode ='a', newline='') as file:
            writer = csv.writer(file)
            for key in dict.keys():
                row = [key,dict[key]['Password'],dict[key]['Address']]
                writer.writerow(row)

    @staticmethod
    def checkMembers(username):
        with open("Members.csv",mode = "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0]==username:
                    return(int(1))
            return (int(0))
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
                if len(row)>0:
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
    #format = {"Username":{"data" : <data>}}
        #format of <data> (nested lists):
        #       [["section1_name","Section_type",("device1_Id","device_type"),("device2_id","device_type")....],["section2_name","device1_Id"."device2_Id"....]....]    
                
    @staticmethod
    def loadHouses():
        with open("Houses.csv",mode = 'r',newline = "") as file:
            dict = {}
            reader = csv.reader(file)
            for row in reader:  #format of csv_file : Username,<Section1_name>%<Section_type>%<Device1_Id>_<Device_type>%<Device2_Id>_<Device2_type>,<Section2_name>_<Device1_Id>_<Device2_Id>,....
                data = []
                for i in range(1,len(row)):
                    lst_temp1 = []
                    lst_temp1 = row[i].strip().split("%")
                    lst_temp2 = []
                    lst_temp2.append(lst_temp1[0])
                    lst_temp2.append(lst_temp1[1])
                    for j in range(2,len(lst_temp1)):
                        temp = lst_temp1[j].strip().split("_")
                        tup_temp = tuple(temp)
                        lst_temp2.append(tup_temp) 
                    data.append(lst_temp2)
                dict[row[0]] = {"data" : data}
        return dict
            
    @staticmethod
    def updateHouses(dict):
        with open("Houses.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            for key in dict.keys():
                row = [key]
                for val in dict[key]["data"]:
                    str_temp = f"{val[0]}%{val[1]}"
                    for i in range(2,len(val)):
                        str_temp2 = f"{val[i][0]}_{val[i][1]}"
                        str_temp = str_temp + f"%{str_temp2}"
                    row.append(str_temp)
                writer.writerow(row)
                
#==========================================================================================================================================
