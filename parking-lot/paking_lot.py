import heapq

class ParkingLot:
    def __init__(self):
        # Initialize your data structures
        self.available_slots = {
            "motorcycle": list(range(1, 21)),    # Slots 1-20 for motorcycles
            "car": list(range(21, 36)),   # Slots 21-35 for cars
            "truck": list(range(36, 46))   # Slots 36-45 for trucks
        }
        # Convert to heaps
        for vehicle_type in self.available_slots:
            heapq.heapify(self.available_slots[vehicle_type])

        self.occupied_slots = {}
    

    def checkIn(self, vehicle_type: str, license_plate: str) -> int:
        """
        Check in a vehicle and allocate a parking slot.
        
        Args:
            vehicle_type: "motorcycle", "car", or "truck"
            license_plate: unique identifier for the vehicle
        
        Returns:
            slot_number: positive integer if successful, -1 if no space
        """
        if vehicle_type not in self.available_slots or not self.available_slots[vehicle_type]:
            return -1
        
        # Get the smallest available slot for the vehicle type
        slot_number = heapq.heappop(self.available_slots[vehicle_type])

        # Store the occupied slot with the vehicle's license plate
        self.occupied_slots[license_plate] = (vehicle_type, slot_number)

        return slot_number
    
    
    def checkOut(self, license_plate: str) -> bool:
        """
        Check out a vehicle and free its parking slot.
        
        Args:
            license_plate: unique identifier for the vehicle
        
        Returns:
            bool: True if successful, False if vehicle not found
        """
        if license_plate not in self.occupied_slots:
            return False
        else:
            vehicle_type, slot_number = self.occupied_slots.pop(license_plate)
            # Add the slot back to the available slots
            heapq.heappush(self.available_slots[vehicle_type], slot_number)
            return True


    
    def getAvailableSlots(self) -> dict:
        """
        Get available slot counts for each vehicle type.
        
        Returns:
            dict: {"motorcycle": int, "car": int, "truck": int}
        """
        return {vehicle_type: len(slots) for vehicle_type, slots in self.available_slots.items()}


if __name__ == "__main__":
    parking_lot = ParkingLot()

    # Check in vehicles
    slot1 = parking_lot.checkIn("car", "ABC123")        # Returns slot number
    slot2 = parking_lot.checkIn("motorcycle", "XYZ789") # Returns slot number
    slot3 = parking_lot.checkIn("truck", "DEF456")      # Returns slot number

    # Check availability
    available = parking_lot.getAvailableSlots()
    print(available)  # Example output: {"motorcycle": 19, "car": 14, "truck": 9}

    # Check out a vehicle
    success = parking_lot.checkOut("ABC123")  # Returns True
    print(success)  # True if successful
    
    # Check availability again
    available = parking_lot.getAvailableSlots()
    print(available)  # Example output: {"motorcycle": 19, "car": 15, "truck": 9}