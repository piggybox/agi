# Parking Lot Management System

## Problem Statement

Design and implement a parking lot management system that can handle vehicles of different sizes. The parking lot has a fixed number of slots, each designed for a specific vehicle size. Your system should efficiently allocate parking slots and track vehicle occupancy.

## Requirements

### Vehicle Types
- **Motorcycle**: Size 1 (can fit in any slot)
- **Car**: Size 2 (needs car or truck slots)
- **Truck**: Size 3 (needs truck slots only)

### Parking Lot Layout
- **Motorcycle slots**: 20 slots (size 1)
- **Car slots**: 15 slots (size 2) 
- **Truck slots**: 10 slots (size 3)

### Core Operations
1. **`checkIn(vehicleType, licensePlate)`**: 
   - Allocate the smallest available slot that can fit the vehicle
   - Return the slot number if successful, or -1 if no space available
   - Store the vehicle information for checkout

2. **`checkOut(licensePlate)`**:
   - Free the slot occupied by the vehicle
   - Return true if successful, false if vehicle not found

3. **`getAvailableSlots()`**:
   - Return the number of available slots for each vehicle type

## Implementation Requirements

```python
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
```

## Example Usage

```python
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
```

## Additional Considerations

1. **Slot Allocation Strategy**: Motorcycles should preferentially use motorcycle slots, but can use car or truck slots if motorcycle slots are full.

2. **Edge Cases**: 
   - What happens when checking in a vehicle that's already parked?
   - What happens when checking out a vehicle that doesn't exist?
   - How do you handle invalid vehicle types?

3. **Time Complexity**: Aim for O(1) average time complexity for both check-in and check-out operations.

4. **Follow-up Questions**:
   - How would you modify the system to handle pricing based on vehicle size and duration?
   - How would you implement a reservation system?
   - How would you handle concurrent access in a multi-threaded environment?

## Evaluation Criteria

- **Correctness**: Does the solution handle all requirements and edge cases?
- **Design**: Is the code well-structured and maintainable?
- **Efficiency**: Are the operations performed in optimal time complexity?
- **Code Quality**: Is the code readable with appropriate variable names and comments?

This question tests object-oriented design, data structure selection, algorithm efficiency, and the ability to handle real-world constraints and edge cases.