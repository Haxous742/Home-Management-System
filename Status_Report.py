import CSV_Handler as csvh

def StatusReport(device_type,section_list):
    device_details = csvh.CSV_Handler.loadDevices()
    print(device_details)
    f = open('report.txt' , 'w')
    f.write(f'Device report of all {device_type} \n')

    for secs in section_list:
        for objs in secs.Device_list:
            for key in device_details:
                if key == objs.device_id:
                    if device_details[key]['type'] == device_type:
                        text = f'The Device {device_details[key]["name"]} is {device_details[key]["status"]} has the following attribute:  {device_details[key]["attributes"]}\n'
                        f.write(text)
    f.close()
    import subprocess
    file_path = "report.txt"
    subprocess.run(['open', file_path])
