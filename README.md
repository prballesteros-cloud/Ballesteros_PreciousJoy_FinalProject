# EcoRide: CLI-Based Bike Rental Management System

An intuitive, command-line interface (CLI) application developed in Python to manage bike rentals, automate fee calculations, and handle real-time inventory tracking. This project serves as the Final Machine Project for Intermediate Programming, demonstrating object-oriented design, persistent file handling, and algorithmic data processing.

---

##  Project Video Demonstration
Click the link below to watch the technical walkthrough and design defense:
*[EcoRide Final Project Demonstration - YouTube](https://youtu.be/vExOrpBHRbE?si=FhOk4gxamuz19aaD
)

---

## 🚀 Features

* *Persistent Data Storage:* Uses text-based file operations to save and load inventory state (data/inventory.txt), ensuring data is preserved even after closing the application.
* *Dynamic Inventory Control:* Administrators can seamlessly insert new stock with automated custom attributes (ID, Brand, Type, and Rates).
* *Smart Transaction Verification:* Implements rigorous data validation to prevent critical errors, such as renting an already checked-out bicycle or returning an unrented asset.
* *Precise Billing Calculations:* Utilizes floating-point precision math to generate exact financial totals based on actual rental durations (e.g., fractional hours like 2.5 hours).
* *Self-Healing File Architecture:* Automatically scans the runtime environment and generates necessary resource folders if missing, mitigating directory crashes.

---

## 🛠️ Core Concepts Demonstrated

1. *Object-Oriented Programming (OOP):* Encapsulation of state and logic within structural data layers (class Bike) and manager architectures (class RentalSystem).
2. *File Handling & Serialization:* Direct parsing, cleaning (strip()), and data restructuring (split()) of raw persistent flat-file CSV models.
3. *Data Structures & Algorithms:* Utilization of dynamic linear lists alongside an $O(n)$ *Linear Search Algorithm* for exact-match ID filtering.

---

## 📁 Repository Structure

```text
DelaCruz_PreciousJoy_FinalProject/
│
├── README.md                  # Project overview, features, and setup guide
│
├── src/                       # Application source modules
│   ├── main.py                # Main executable entry point and CLI view loop
│   ├── manager.py             # Business logic layer and transactional processes
│   └── models.py              # Data structure and object mappings
│
└── data/                      # Local data persistency container
    └── inventory.txt          # Auto-generated database storage file
