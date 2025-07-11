class ParkingLot:
    def __init__(self):
        # Initialize your data structures
        pass
    
    def checkIn(self, vehicle_type: str, license_plate: str) -> int:
        """
        Check in a vehicle and allocate a parking slot.
        
        Args:
            vehicle_type: "motorcycle", "car", or "truck"
            license_plate: unique identifier for the vehicle
        
        Returns:
            slot_number: positive integer if successful, -1 if no space
        """
        pass
    
    def checkOut(self, license_plate: str) -> bool:
        """
        Check out a vehicle and free its parking slot.
        
        Args:
            license_plate: unique identifier for the vehicle
        
        Returns:
            bool: True if successful, False if vehicle not found
        """
        pass
    
    def getAvailableSlots(self) -> dict:
        """
        Get available slot counts for each vehicle type.
        
        Returns:
            dict: {"motorcycle": int, "car": int, "truck": int}
        """
        pass


if __name__ == "__main__":
    parking_lot = ParkingLot()

    # Check in vehicles
    slot1 = parking_lot.checkIn("car", "ABC123")        # Returns slot number
    slot2 = parking_lot.checkIn("motorcycle", "XYZ789") # Returns slot number
    slot3 = parking_lot.checkIn("truck", "DEF456")      # Returns slot number

    # Check availability
    available = parking_lot.getAvailableSlots()
    # Returns: {"motorcycle": 19, "car": 14, "truck": 9}

    # Check out a vehicle
    success = parking_lot.checkOut("ABC123")  # Returns True