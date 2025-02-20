# Vehicle Rental Management System

## Overview:
Vehicle Tracker is a Python-based CRUD (Create, Read, Update, Delete) application for managing vehicle data. It enables users to search, add, update, delete, rent, and return vehicles efficiently. The program utilizes dictionaries to store data and the PrettyTable module for structured tabular output.

## Features
### 🚗 Vehicle Management
- **Show Vehicle Data**
  - View all vehicle details
  - Search vehicles by license plate, type, or tax status
  - Display vehicles with expired taxes
- **Add Vehicle**
  - Enter vehicle details such as license plate, type, brand, tax status, and tax validity period
- **Update Vehicle Data**
  - Modify registered vehicle information
- **Delete Vehicle**
  - Remove vehicles that are no longer needed

### 📋 Rental System
- **Rent a Vehicle**
  - Record rental information (renter’s name, rental date, and return date)
- **Return a Vehicle**
  - Process vehicle returns and update availability
- **Check Availability**
  - Verify vehicle availability based on license plate or date (odd-even system)

### 📊 Reports & Insights
- Generate reports on:
  - All registered vehicles
  - Vehicles currently rented
  - Vehicles with expired tax

## Requirements
- Python 3.x
- PrettyTable module

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/Vehicle-Tracker.git
2. **Navigate to the Project Directory**
   
   cd Vehicle-Tracker
4. **Install Dependencies**
   
   pip install prettytable
6. **Run the Program**
   
   python vehicle_tracker.py

## Menu
Upon running the script, you will be presented with the main menu:
```
Welcome to Vehicle Rental Management System

Main Menu:
1. Show Vehicle Data
  1.1. View All Vehicles
  1.2. Search by License Plate
  1.3. Search by Vehicle Type
  1.4. Search by Tax Status
  1.5. Check Availability (Odd-Even System)
  1.6. Find Tax Costs
    1.6.1. Show Lowest Tax Cost
    1.6.2. Show Highest Tax Cost
    1.6.3. Sort Vehicles by Lowest Tax
    1.6.4. Sort Vehicles by Highest Tax
2. Add New Vehicle
3. Update Vehicle Data
4. Delete Vehicle
5. Rental Management
  5.1 Rent a Vehicle
  5.2. Return a Vehicle
  5.3. View Rental Records
6. Exit
```

## Data Structure
The vehicle data is stored in a dictionary with the following keys:
- `plat`: List of vehicle license plates.
- `jenis`: List of vehicle types (car, motorcycle, truck, etc.).
- `merek`: List of vehicle brands.
- `status_pajak`: List of tax statuses (active, expired).
- `harga_pajak` : Price of the tax vehicle (in rupiah)
- `masa_berlaku`: List of tax validity periods.

## Contribution
Contributions are welcome! Feel free to suggest improvements, report issues, or submit pull requests on GitHub.

Developed by: Nabila Lailinajma 
