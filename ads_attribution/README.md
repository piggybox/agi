## Programming Interview Question: Ads Attribution System

### Problem Statement

You need to build an ads attribution system that processes two data streams:
1. **Impression stream**: When users view ads
2. **Conversion stream**: When users complete desired actions (purchases, signups, etc.)

The system should attribute each conversion to the **last impression** that occurred within the **last N hours** before the conversion for the same user.

### Data Structures

```python
class Impression:
    def __init__(self, user_id: str, ad_id: str, timestamp: int):
        self.user_id = user_id
        self.ad_id = ad_id
        self.timestamp = timestamp  # Unix timestamp in seconds

class Conversion:
    def __init__(self, user_id: str, conversion_id: str, timestamp: int, value: float):
        self.user_id = user_id
        self.conversion_id = conversion_id
        self.timestamp = timestamp  # Unix timestamp in seconds
        self.value = value  # conversion value (e.g., purchase amount)

class Attribution:
    def __init__(self, conversion_id: str, ad_id: str, user_id: str, 
                 impression_timestamp: int, conversion_timestamp: int):
        self.conversion_id = conversion_id
        self.ad_id = ad_id
        self.user_id = user_id
        self.impression_timestamp = impression_timestamp
        self.conversion_timestamp = conversion_timestamp
```

### Requirements

Implement a class `AttributionSystem` with the following methods:

```python
class AttributionSystem:
    def __init__(self, attribution_window_hours: int):
        """
        Initialize the attribution system
        
        Args:
            attribution_window_hours: Number of hours to look back for impressions
        """
        pass
    
    def process_impression(self, impression: Impression) -> None:
        """
        Process a new impression event
        
        Args:
            impression: The impression event to process
        """
        pass
    
    def process_conversion(self, conversion: Conversion) -> Optional[Attribution]:
        """
        Process a conversion event and return attribution if found
        
        Args:
            conversion: The conversion event to process
            
        Returns:
            Attribution object if a qualifying impression is found, None otherwise
        """
        pass
    
    def cleanup_old_impressions(self, current_timestamp: int) -> None:
        """
        Remove impressions older than the attribution window to prevent memory leaks
        
        Args:
            current_timestamp: Current system timestamp
        """
        pass
```

### Example Usage

```python
# Initialize system with 24-hour attribution window
system = AttributionSystem(attribution_window_hours=24)

# Process some impressions
system.process_impression(Impression("user1", "ad123", 1000))
system.process_impression(Impression("user1", "ad456", 2000))
system.process_impression(Impression("user2", "ad789", 1500))

# Process conversions
attribution1 = system.process_conversion(Conversion("user1", "conv1", 3000, 25.99))
# Should return Attribution with ad_id="ad456" (last impression for user1)

attribution2 = system.process_conversion(Conversion("user2", "conv2", 90000, 15.50))
# Should return None (impression too old, outside 24-hour window)
```

### Follow-up Questions

1. **Scalability**: How would you modify this system to handle millions of events per second?

2. **Memory Management**: What strategies would you use to prevent memory leaks in a long-running system?

3. **Data Consistency**: How would you handle out-of-order events (impression arriving after conversion)?

4. **Attribution Models**: How would you extend this to support different attribution models (first-touch, multi-touch, etc.)?

5. **Distributed Systems**: How would you implement this across multiple servers/processes?

### Expected Time Complexity
- `process_impression`: O(log n) where n is number of impressions per user
- `process_conversion`: O(log n) where n is number of impressions per user
- `cleanup_old_impressions`: O(m) where m is number of users with old impressions

### Evaluation Criteria
- **Correctness**: Proper attribution logic and edge case handling
- **Efficiency**: Optimal time/space complexity
- **Code Quality**: Clean, readable, and maintainable code
- **System Design**: Consideration of real-world scalability challenges

This question tests data structure knowledge, algorithm design, system scalability thinking, and practical software engineering skills commonly needed in ad-tech companies.