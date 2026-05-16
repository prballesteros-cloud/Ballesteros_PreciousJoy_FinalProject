import os
from models import Bike

class RentalSystem:
    def __init__(self):
        self.inventory = []
        self.file_path = "data/inventory.txt"
        self.ensure_data_folder()
        self.load_from_file()

    def ensure_data_folder(self):
        """Creates the data folder if it doesn't exist."""
        if not os.path.exists("data"):
            os.makedirs("data")

    def load_from_file(self):
        """FILE HANDLING: Loads data from text file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                for line in f:
                    d = line.strip().split(",")
                    if len(d) == 5:
                        # Logic to convert string 'True' back to Boolean
                        is_avail = d[4] == "True"
                        self.inventory.append(Bike(d[0], d[1], d[2], d[3], is_avail))

    def save_to_file(self):
        """FILE HANDLING: Saves list data back to text file."""
        with open(self.file_path, "w") as f:
            for b in self.inventory:
                f.write(b.format_for_file() + "\n")

    def find_bike(self, bid):
        """ALGORITHM: Linear Search to find a bike by ID."""
        for b in self.inventory:
            if b.bike_id == bid:
                return b
        return