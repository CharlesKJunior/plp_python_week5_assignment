# plp_python_week5_assignment
# README for Assignment 1: Smartphone OOP Design

## Overview
This project demonstrates Object-Oriented Programming (OOP) in Python using a `Smartphone` class and its subclass `Smartwatch`. It showcases concepts like class creation, attributes, methods, constructors, inheritance, and encapsulation.

## Features
### Smartphone Class
- **Attributes**: `brand`, `model`, `battery`, `storage`, `apps`
- **Methods**:
  - `install_app(app_name)`: Installs an app and reduces storage.
  - `charge()`: Fully charges the smartphone.
  - `use(hours)`: Simulates phone usage and reduces battery.
  - `get_status()`: Displays the current status including battery, storage, and installed apps.

### Smartwatch Class (Inherits from Smartphone)
- **Additional Attributes**: `heart_rate`
- **Additional Methods**:
  - `track_heart_rate(rate)`: Records and prints the user's heart rate.

## How to Run
1. Make sure Python is installed on your system.
2. Save the code in a file named `assignment1.py`.
3. Run the script:
   ```bash
   python assignment1.py
   ```

## Example Output
```
Pixel 8 Pro -> Battery: 100%, Storage: 128GB
Installed apps: None
App 'Instagram' installed on 8 Pro. 📱
Used 8 Pro for 3 hour(s). 🔄
Pixel 8 Pro -> Battery: 70%, Storage: 127GB
Installed apps: Instagram
Galaxy Watch 6 -> Battery: 80%, Storage: 32GB
Installed apps: None
Galaxy Watch 6 is tracking heart rate: 72 bpm ❤️
App 'Health Monitor' installed on Galaxy Watch 6. 📱
Galaxy Watch 6 -> Battery: 80%, Storage: 31GB
Installed apps: Health Monitor
```

---



# README for Activity 2: Polymorphism Challenge

## Overview
This script demonstrates **polymorphism** using a base `Vehicle` class and subclasses (`Car`, `Plane`, and `Boat`) that override the `move()` method with different implementations.

## Classes
- **Vehicle (Base Class)**: Contains an abstract `move()` method.
- **Car (Subclass)**: Implements `move()` to simulate driving.
- **Plane (Subclass)**: Implements `move()` to simulate flying.
- **Boat (Subclass)**: Implements `move()` to simulate sailing.

## How to Run
1. Save the code in a file named `activity2.py`.
2. Run the script:
   ```bash
   python activity2.py
   ```

## Expected Output
```
Driving on the road 🚗
Flying through the sky ✈️
Sailing on the water ⛵
```

## Concepts Practiced
- Polymorphism: All objects share the same interface (`move()`), but behave differently.
- Inheritance: All vehicle types inherit from the same parent class.

---
