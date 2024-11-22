from CSV_Handler import CSV_Handler as CSV

dict = {"Doland Trump":{"Password":"DonaldTrumpSucks","Address":"The White House","Houses":["House1_Id","House1_Id"]},
        "Osama Bin Laden":{"Password":"9/11","Address":"World Trade center","Houses":["House1_Id","House2_Id"]}}
 
CSV.updateMembers(dict)

dict2 = {"B01" : {"name" : "Bedroom_Bulb", "type":"bulb", "status":"On", "attributes":{"brightness":"69","colour":"green"}}}

CSV.updateDevices(dict2)

dict3 = {"H10":{"name":"House_1","data":[["Bedroom","B01","F02"],["Bathroom","E01","D02"]]}}

CSV.updateHouses(dict3)

print(CSV.loadMembers())
print(CSV.loadDevices())
print(CSV.loadHouses())
