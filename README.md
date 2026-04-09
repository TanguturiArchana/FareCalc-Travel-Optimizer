# FareCalc Travel Optimizer

## Description

The **FareCalc Travel Optimizer** is a Python-based console application designed for a ride-sharing service like **CityCab**. It calculates ride fares dynamically based on distance, vehicle type, and time of travel. The system applies surge pricing during peak hours and generates a detailed ride receipt.

## Key Features

* Distance-based Fare Calculation
* Vehicle Type Pricing (Economy, Premium, SUV)
* Peak Hour Surge Pricing (5 PM – 8 PM)
* Error Handling for Invalid Inputs
* Formatted Ride Receipt Display
* Ride History Tracking
* File-based Receipt Storage

## Technologies Used

* Python
* Dictionaries
* Functions
* Exception Handling
* File Handling

## How It Works

* User enters distance, vehicle type, and travel time
* System calculates base fare using rate per km
* Applies surge multiplier during peak hours
* Displays total fare with receipt details
* Saves receipt to a file

## How to Run

```bash
python FareCalc.py
```

