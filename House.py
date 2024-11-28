class Home:
    def __init__(self):
        self.house = {}
        
    def add_house(self, house_id, name):
        if house_id in self.house:
            return f"House with ID {house_id} already exists."
        
        self.house[house_id] = {
            "name": name,
            "data": []
        }
        return f"House '{name}' with ID {house_id} added successfully."

    def add_section(self, house_id, section_name, *device_ids):
        if house_id not in self.house:
            return f"House ID {house_id} not found."

        section = [section_name] + list(device_ids)
        self.house[house_id]["data"].append(section)
        return f"Section '{section_name}' added to house {house_id}."

    def remove_section(self, house_id, section_name):
        if house_id not in self.house:
            return f"House ID {house_id} not found."
        
        house = self.house[house_id]
        house["data"] = [section for section in house["data"] if section[0] != section_name]
        return f"Section '{section_name}' removed from house {house_id}."
    def _update_csv(self, filename, house_id, name):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([house_id, name])
        #im not so sure about the subclasses cuz i feel like i will need functions from device class also
