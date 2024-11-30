import csv

class Home:
    def __init__(self, filename):
        self.filename = filename

    def add_section(self, house_id, section_name, *device_ids):
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([house_id, section_name, *device_ids])
            return f"Section '{section_name}' added to house {house_id}."
        except Exception as e:
            return f"Error while adding section: {e}"

    def remove_section(self, house_id, section_name):
        try:
            updated_rows = []
            section_removed = False

            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == house_id and row[1] == section_name:
                        section_removed = True
                    else:
                        updated_rows.append(row)

            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if section_removed:
                return f"Section '{section_name}' removed from house {house_id}."
            return f"Section '{section_name}' not found in house {house_id}."
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
class Bedroom(Home):
    '''def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Bedroom", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Bedroom", device_id)'''


class Kitchen(Home):
    '''def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Kitchen", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Kitchen", device_id)'''


class Garage(Home):
   ''' def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Garage", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Garage", device_id)'''


class LivingRoom(Home):
    '''def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Living Room", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Living Room", device_id)'''


class Bathroom(Home):
   ''' def add_device(self, house_id, device_id):
        return super().add_device(house_id, "Bathroom", device_id)
    
    def remove_device(self, house_id, device_id):
        return super().remove_device(house_id, "Bathroom", device_id)'''
