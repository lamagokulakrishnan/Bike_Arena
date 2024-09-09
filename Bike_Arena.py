class LamaBikeArena:
    def __init__(self):
        self.bikes = {
            'YAM001': {'company': 'Yamaha', 'model': 'YZF R15 V3', 'launch_year': 2018, 'engine_capacity': 155, 'fuel_capacity': 11, 'mileage': 40, 'brake_system': 'Dual Disc', 'rpm': 10000, 'price': 170000, 'sold': False},
            'YAM002': {'company': 'Yamaha', 'model': 'FZ S V3', 'launch_year': 2019, 'engine_capacity': 149, 'fuel_capacity': 13, 'mileage': 45, 'brake_system': 'Single Disc', 'rpm': 8000, 'price': 110000, 'sold': False},
            'YAM003': {'company': 'Yamaha', 'model': 'MT 15', 'launch_year': 2019, 'engine_capacity': 155, 'fuel_capacity': 10, 'mileage': 48, 'brake_system': 'Dual Disc', 'rpm': 10000, 'price': 160000, 'sold': False},
            'YAM004': {'company': 'Yamaha', 'model': 'FZ25', 'launch_year': 2017, 'engine_capacity': 249, 'fuel_capacity': 14, 'mileage': 43, 'brake_system': 'Dual Disc', 'rpm': 9000, 'price': 150000, 'sold': False},
            'YAM005': {'company': 'Yamaha', 'model': 'Fascino', 'launch_year': 2015, 'engine_capacity': 113, 'fuel_capacity': 5.2, 'mileage': 66, 'brake_system': 'Drum', 'rpm': 7500, 'price': 80000, 'sold': False},
            # Bajaj bikes
            'BAJ001': {'company': 'Bajaj', 'model': 'Pulsar 150', 'launch_year': 2001, 'engine_capacity': 149, 'fuel_capacity': 15, 'mileage': 50, 'brake_system': 'Disc', 'rpm': 9000, 'price': 120000, 'sold': False},
            'BAJ002': {'company': 'Bajaj', 'model': 'Dominar 400', 'launch_year': 2016, 'engine_capacity': 373, 'fuel_capacity': 13, 'mileage': 27, 'brake_system': 'Dual Disc', 'rpm': 8500, 'price': 240000, 'sold': False},
            'BAJ003': {'company': 'Bajaj', 'model': 'Avenger 220', 'launch_year': 2010, 'engine_capacity': 220, 'fuel_capacity': 14, 'mileage': 40, 'brake_system': 'Disc', 'rpm': 8500, 'price': 130000, 'sold': False},
            'BAJ004': {'company': 'Bajaj', 'model': 'Platina 110', 'launch_year': 2006, 'engine_capacity': 115, 'fuel_capacity': 11, 'mileage': 80, 'brake_system': 'Drum', 'rpm': 7500, 'price': 70000, 'sold': False},
            'BAJ005': {'company': 'Bajaj', 'model': 'CT 100', 'launch_year': 2004, 'engine_capacity': 102, 'fuel_capacity': 10.5, 'mileage': 90, 'brake_system': 'Drum', 'rpm': 7500, 'price': 55000, 'sold': False},
            # Royal Enfield bikes
            'RE001': {'company': 'Royal Enfield', 'model': 'Classic 350', 'launch_year': 2009, 'engine_capacity': 346, 'fuel_capacity': 13.5, 'mileage': 35, 'brake_system': 'Disc', 'rpm': 5250, 'price': 210000, 'sold': False},
            'RE002': {'company': 'Royal Enfield', 'model': 'Bullet 350', 'launch_year': 1931, 'engine_capacity': 346, 'fuel_capacity': 13.5, 'mileage': 37, 'brake_system': 'Drum', 'rpm': 5250, 'price': 170000, 'sold': False},
            'RE003': {'company': 'Royal Enfield', 'model': 'Himalayan', 'launch_year': 2016, 'engine_capacity': 411, 'fuel_capacity': 15, 'mileage': 30, 'brake_system': 'Disc', 'rpm': 6500, 'price': 250000, 'sold': False},
            'RE004': {'company': 'Royal Enfield', 'model': 'Interceptor 650', 'launch_year': 2018, 'engine_capacity': 648, 'fuel_capacity': 13.7, 'mileage': 25, 'brake_system': 'Dual Disc', 'rpm': 7100, 'price': 300000, 'sold': False},
            'RE005': {'company': 'Royal Enfield', 'model': 'Meteor 350', 'launch_year': 2020, 'engine_capacity': 349, 'fuel_capacity': 15, 'mileage': 35, 'brake_system': 'Disc', 'rpm': 6100, 'price': 220000, 'sold': False},
            # TVS bikes
            'TVS001': {'company': 'TVS', 'model': 'Apache RTR 160', 'launch_year': 2006, 'engine_capacity': 159, 'fuel_capacity': 12, 'mileage': 45, 'brake_system': 'Disc', 'rpm': 8500, 'price': 120000, 'sold': False},
            'TVS002': {'company': 'TVS', 'model': 'Ntorq 125', 'launch_year': 2018, 'engine_capacity': 124, 'fuel_capacity': 5, 'mileage': 45, 'brake_system': 'Drum', 'rpm': 7500, 'price': 85000, 'sold': False},
            'TVS003': {'company': 'TVS', 'model': 'Jupiter', 'launch_year': 2013, 'engine_capacity': 109, 'fuel_capacity': 6, 'mileage': 62, 'brake_system': 'Drum', 'rpm': 7500, 'price': 75000, 'sold': False},
            'TVS004': {'company': 'TVS', 'model': 'Sport', 'launch_year': 2007, 'engine_capacity': 109, 'fuel_capacity': 10, 'mileage': 70, 'brake_system': 'Drum', 'rpm': 7500, 'price': 65000, 'sold': False},
            'TVS005': {'company': 'TVS', 'model': 'Radeon', 'launch_year': 2018, 'engine_capacity': 109, 'fuel_capacity': 10, 'mileage': 70, 'brake_system': 'Drum', 'rpm': 7500, 'price': 70000, 'sold': False},
            # Suzuki bikes
            'SUZ001': {'company': 'Suzuki', 'model': 'Gixxer SF', 'launch_year': 2015, 'engine_capacity': 155, 'fuel_capacity': 12, 'mileage': 45, 'brake_system': 'Disc', 'rpm': 9500, 'price': 130000, 'sold': False},
            'SUZ002': {'company': 'Suzuki', 'model': 'Access 125', 'launch_year': 2007, 'engine_capacity': 124, 'fuel_capacity': 5.6, 'mileage': 64, 'brake_system': 'Drum', 'rpm': 7500, 'price': 80000, 'sold': False},
            'SUZ003': {'company': 'Suzuki', 'model': 'Intruder', 'launch_year': 2017, 'engine_capacity': 155, 'fuel_capacity': 11, 'mileage': 44, 'brake_system': 'Disc', 'rpm': 9000, 'price': 125000, 'sold': False},
            'SUZ004': {'company': 'Suzuki', 'model': 'Burgman Street 125', 'launch_year': 2018, 'engine_capacity': 124, 'fuel_capacity': 5.6, 'mileage': 54, 'brake_system': 'Drum', 'rpm': 7500, 'price': 90000, 'sold': False},
            'SUZ005': {'company': 'Suzuki', 'model': 'Hayabusa', 'launch_year': 1999, 'engine_capacity': 1340, 'fuel_capacity': 20, 'mileage': 15, 'brake_system': 'Dual Disc', 'rpm': 9500, 'price': 1650000, 'sold': False},
            # KTM bikes
            'KTM001': {'company': 'KTM', 'model': 'Duke 200', 'launch_year': 2012, 'engine_capacity': 199, 'fuel_capacity': 10.2, 'mileage': 35, 'brake_system': 'Disc', 'rpm': 10000, 'price': 185000, 'sold': False},
            'KTM002': {'company': 'KTM', 'model': 'Duke 390', 'launch_year': 2013, 'engine_capacity': 373, 'fuel_capacity': 13.5, 'mileage': 25, 'brake_system': 'Dual Disc', 'rpm': 9000, 'price': 310000, 'sold': False},
            'KTM003': {'company': 'KTM', 'model': 'RC 200', 'launch_year': 2014, 'engine_capacity': 199, 'fuel_capacity': 10, 'mileage': 35, 'brake_system': 'Disc', 'rpm': 10000, 'price': 215000, 'sold': False},
            'KTM004': {'company': 'KTM', 'model': 'RC 390', 'launch_year': 2014, 'engine_capacity': 373, 'fuel_capacity': 10, 'mileage': 25, 'brake_system': 'Dual Disc', 'rpm': 9000, 'price': 340000, 'sold': False},
            'KTM005': {'company': 'KTM', 'model': 'Adventure 390', 'launch_year': 2019, 'engine_capacity': 373, 'fuel_capacity': 14.5, 'mileage': 25, 'brake_system': 'Dual Disc', 'rpm': 9000, 'price': 350000, 'sold': False},
            # Honda bikes
            'HON001': {'company': 'Honda', 'model': 'CB Hornet 160R', 'launch_year': 2015, 'engine_capacity': 162, 'fuel_capacity': 12, 'mileage': 50, 'brake_system': 'Disc', 'rpm': 8500, 'price': 125000, 'sold': False},
            'HON002': {'company': 'Honda', 'model': 'Activa 6G', 'launch_year': 2020, 'engine_capacity': 109, 'fuel_capacity': 5.3, 'mileage': 60, 'brake_system': 'Drum', 'rpm': 7500, 'price': 75000, 'sold': False},
            'HON003': {'company': 'Honda', 'model': 'CB Shine', 'launch_year': 2006, 'engine_capacity': 124, 'fuel_capacity': 10.5, 'mileage': 65, 'brake_system': 'Drum', 'rpm': 7500, 'price': 85000, 'sold': False},
            'HON004': {'company': 'Honda', 'model': 'Hness CB350', 'launch_year': 2020, 'engine_capacity': 348, 'fuel_capacity': 15, 'mileage': 35, 'brake_system': 'Disc', 'rpm': 6500, 'price': 215000, 'sold': False},
            'HON005': {'company': 'Honda', 'model': 'CBR 250R', 'launch_year': 2011, 'engine_capacity': 249, 'fuel_capacity': 13, 'mileage': 30, 'brake_system': 'Disc', 'rpm': 8500, 'price': 195000, 'sold': False}
            # Add other bikes here...
        }
        self.sold_bikes = {}
        self.payments = []

    def add_bike(self, bike_id, company, model, launch_year, engine_capacity, fuel_capacity, mileage, brake_system, rpm, price):
        if bike_id in self.bikes:
            print("Bike ID already exists.")
            return False
        self.bikes[bike_id] = {'company': company, 'model': model, 'launch_year': launch_year, 'engine_capacity': engine_capacity, 'fuel_capacity': fuel_capacity, 'mileage': mileage, 'brake_system': brake_system, 'rpm': rpm, 'price': price, 'sold': False}
        print("The bike was added successfully.")
        return True

    def remove_bike(self, bike_id):
        if bike_id in self.bikes:
            del self.bikes[bike_id]
            print("The bike was removed successfully.")
            return True
        print("Bike ID not found.")
        return False

    def sell_bike(self, bike_id, payment_type):
        if bike_id in self.bikes and not self.bikes[bike_id]['sold']:
            self.bikes[bike_id]['sold'] = True
            self.sold_bikes[bike_id] = self.bikes[bike_id]
            self.payments.append({'bike_id': bike_id, 'payment_type': payment_type, 'price': self.bikes[bike_id]['price']})
            return True
        return False

    def display_companies(self):
        companies = set(bike['company'] for bike in self.bikes.values())
        for i, company in enumerate(companies, 1):
            print(f"{i}. {company}")
        return list(companies)

    def display_bikes_by_company(self, company=None, sold=False):
        if company:
            bikes_to_display = {k: v for k, v in self.bikes.items() if v['company'] == company and v['sold'] == sold}
        else:
            bikes_to_display = {k: v for k, v in self.bikes.items() if v['sold'] == sold}
        for bike_id, bike in bikes_to_display.items():
            print(f"\nBike ID: {bike_id}, \nCompany: {bike['company']}, \nModel: {bike['model']}, \nLaunch year: {bike['launch_year']}, \nEngine capacity: {bike['engine_capacity']}, \nFuel capacity: {bike['fuel_capacity']}, \nMileage: {bike['mileage']}, \nRPM: {bike['rpm']}, \nPrice: {bike['price']}")

    def display_payments(self):
        if not self.payments:
            print("No payments recorded yet.")
            return
        for payment in self.payments:
            print(f"\nBike ID: {payment['bike_id']}, \nPayment Type: {payment['payment_type']}, \nPrice: {payment['price']}")

def admin_interface(showroom):
    while True:
        print("\nAdmin Interface")
        print("1. Display Sold Bikes")
        print("2. Display Unsold Bikes")
        print("3. Display Payment Details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            showroom.display_bikes_by_company(sold=True)
        elif choice == '2':
            showroom.display_bikes_by_company(sold=False)
        elif choice == '3':
            showroom.display_payments()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def user_interface(showroom):
    while True:
        print("\nUser Interface")
        print("1. Add Bike")
        print("2. Remove Bike")
        print("3. Display Unsold Bikes")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bike_id = input("Enter Bike ID: ")
            company = input("Enter Bike Company: ")
            model = input("Enter Bike Model: ")
            launch_year = input("Enter the Launch Year: ")
            engine_capacity = input("Enter the Engine Capacity: ")
            fuel_capacity = input("Enter the Fuel Capacity: ")
            mileage = input("Enter the Mileage: ")
            brake_system = input("Enter the Brake System: ")
            rpm = input("Enter the RPM: ")
            price = float(input("Enter Bike Price: "))
            showroom.add_bike(bike_id, company, model, launch_year, engine_capacity, fuel_capacity, mileage, brake_system, rpm, price)
        elif choice == '2':
            bike_id = input("Enter Bike ID to remove: ")
            showroom.remove_bike(bike_id)
        elif choice == '3':
            showroom.display_bikes_by_company(sold=False)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def customer_interface(showroom):
    while True:
        print("\nCustomer Interface")
        print("1. Display Unsold Bikes")
        print("2. Buy a Bike")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            companies = showroom.display_companies()
            company_choice = int(input("Select a company: "))
            selected_company = companies[company_choice - 1]
            showroom.display_bikes_by_company(selected_company, sold=False)
        elif choice == '2':
            bike_id = input("Enter Bike ID to buy: ")
            if bike_id in showroom.bikes and not showroom.bikes[bike_id]['sold']:
                print(f"Bike Price: {showroom.bikes[bike_id]['price']}")
                confirm = input("Do you want to buy this bike? (yes/no): ")
                if confirm.lower() == 'yes':
                    payment_type = input("Enter payment type (cash/card): ")
                    if showroom.sell_bike(bike_id, payment_type):
                        print("Thank you for buying the bike!")
                    else:
                        print("Failed to process the purchase.")
                else:
                    print("Thank you for visiting the showroom.")
            else:
                print("Invalid Bike ID or the bike is already sold.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    showroom = LamaBikeArena()
    
    while True:
        print("\nMain Menu")
        print("1. Admin Interface")
        print("2. User Interface")
        print("3. Customer Interface")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_interface(showroom)
        elif choice == '2':
            user_interface(showroom)
        elif choice == '3':
            customer_interface(showroom)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
