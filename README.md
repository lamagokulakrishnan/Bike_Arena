# Bike Arena 🏍️  
*Bike Showroom Management System*

## Project Overview  
**Bike Arena** is a Python-based showroom management system that simplifies the management of bike inventories, sales, and customer interactions. It features three distinct interfaces: Admin, User, and Customer. Each interface is designed to facilitate specific tasks, ensuring a smooth operation for both the showroom staff and customers.

## Features  

### 1. Admin Interface  
- **Check Unsold and Sold Bikes**: View the list of bikes available or sold in the showroom.
- **Manage Payment Methods**: Process payments for sold bikes using cash or card options.
- **Exit**: Close the Admin Interface.

### 2. User Interface  
- **Add a Bike**: Add new bikes to the showroom with details like:
  - Bike ID  
  - Bike Model  
  - Bike Name  
  - Company Name  
  - Fuel Type  
  - Engine Capacity  
  - Mileage  
  - Brake System  
  - Price
- **Remove a Bike**: Remove bikes from the showroom inventory.
- **View Unsold Bikes**: Check out the list of available bikes in the showroom.
- **Exit**: Close the User Interface.

### 3. Customer Interface  
- **View Unsold Bikes**: Display all available bikes for purchase.
- **Buy a Bike**: 
  - Select a bike by entering its ID.
  - The price is displayed, and the customer can decide whether to proceed with the purchase.
  - Payment options include cash or card.
  - If the customer chooses not to purchase, they are thanked for their visit.
- **Exit**: Close the Customer Interface.

## Technologies Used  
- **Programming Language**: Python 3.x
- **Database**: MS SQL (or any SQL-based database)

Here’s the **Installation Instructions** section formatted for your **Bike Arena** project:

---

## Installation Instructions  

### Prerequisites  
Before running the **Bike Arena** project, ensure you have the following:

- **Python 3.x** installed on your machine
- **Virtual environment** (optional but recommended)

### Steps to Set Up the Project  

1. **Clone the repository**:  
   Download the project by cloning the GitHub repository to your local machine using the following command:
   ```bash
   git clone https://github.com/lamagokulakrishnan/bike-arena.git
   cd bike-arena
   ```

2. **Create a virtual environment** (optional but recommended):  
   Set up a virtual environment to manage dependencies:
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:  
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install project dependencies**:  
   Install all required packages by using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Python script**:  
   Execute the main script to start the application:
   ```bash
   python bike_arena.py
   ```

6. **Access the Interfaces**:  
 
   Follow the prompts in the terminal to interact with the Admin, User, or Customer interfaces.

---
## Usage  
- **Admin Interface**: Manage inventory, view bike statuses, and handle payments.
- **User Interface**: Add or remove bikes and view unsold bikes.
- **Customer Interface**: View available bikes and purchase with payment options.

## Requirements File  
The project dependencies are listed in the `requirements.txt` file. Run the following command to install all the necessary packages:

```bash
pip install -r requirements.txt
```

### Example of `requirements.txt`  
```txt
Flask==2.1.2
requests==2.26.0
```

Update this file with any additional dependencies as necessary.

 
