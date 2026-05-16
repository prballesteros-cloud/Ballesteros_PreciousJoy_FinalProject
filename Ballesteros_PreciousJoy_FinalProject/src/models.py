class Bike:
    def __init__(self, bike_id, brand, bike_type, rate, available=True):
        self.bike_id = bike_id
        self.brand = brand
        self.bike_type = bike_type
        self.rate = float(rate)
        self.available = available

    def format_for_file(self):
        """Converts object data into a CSV string for file storage."""
        return f"{self.bike_id},{self.brand},{self.bike_type},{self.rate},{self.available}" 