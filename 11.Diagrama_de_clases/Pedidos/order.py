from customers import Customers
from employees import Employees
from shippers import Shippers

class Order:
    id_order = 0

    # --- Constructor de clase ---
    def __init__(self, customer_id, employee_id, order_date, required_date, shipped_date, 
                 ship_via, freight, ship_name, ship_adress, ship_city, ship_region, 
                 ship_postal_code, ship_country):
        Order.id_order +=1
        self._id_order = Order.id_order
        self._customer_id  = customer_id
        self._employee_id = employee_id
        self._order_date = order_date
        self._required_date = required_date
        self._shipped_date = shipped_date
        self._ship_via =ship_via
        self._freigth = freight
        self._ship_name = ship_name
        self._ship_adress = ship_adress
        self._ship_city = ship_city
        self._ship_region = ship_region
        self._ship_postal_code = ship_postal_code
        self._ship_country = ship_country
    # --- Fin constructor de clase ---

    # --- Métodos Set ---
    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_order_date(self, order_date):
        self._order_date = order_date

    def set_required_date(self, required_date):
        self._required_date = required_date

    def set_shipped_date(self, shipped_date):
        self._shipped_date = shipped_date

    def set_ship_via(self, ship_via):
        self._ship_via = ship_via

    def set_freight(self, freight):
        self._freight = freight

    def set_ship_name(self, ship_name):
        self._ship_name = ship_name

    def set_ship_address(self, ship_address):
        self._ship_address = ship_address

    def set_ship_city(self, ship_city):
        self._ship_city = ship_city

    def set_ship_region(self, ship_region):
        self._ship_region = ship_region

    def set_ship_postal_code(self, ship_postal_code):
        self._ship_postal_code = ship_postal_code

    def set_ship_country(self, ship_country):
        self._ship_country = ship_country
    # --- Fin Métodos Set ---

    # --- Métodos Get ---
    def get_customer_id(self):
        return self._customer_id

    def get_employee_id(self):
        return self._employee_id

    def get_order_date(self):
        return self._order_date

    def get_required_date(self):
        return self._required_date

    def get_shipped_date(self):
        return self._shipped_date

    def get_ship_via(self):
        return self._ship_via

    def get_freight(self):
        return self._freight

    def get_ship_name(self):
        return self._ship_name

    def get_ship_address(self):
        return self._ship_address

    def get_ship_city(self):
        return self._ship_city

    def get_ship_region(self):
        return self._ship_region

    def get_ship_postal_code(self):
        return self._ship_postal_code

    def get_ship_country(self):
        return self._ship_country
    # --- Fin Métodos Get ---

    # --- Método string ---
    def __str__(self) -> str:
        return f"""
        Order N° {self._id_order}
            Customer id: {self._customer_id}
            Employee id: {self._employee_id}
            Order date: {self._order_date}
            Required date: {self._required_date}
            Shipped date: {self._shipped_date}
            Ship via: {self._ship_via}
            Freight: {self._freigth}
            Ship name: {self._ship_name}
            Ship address: {self._ship_adress}
            Ship city: {self._ship_city}
            Ship region: {self._ship_region}
            Ship postal code: {self._ship_postal_code}
            Ship country: {self._ship_country}
        """

if __name__ == "__main__":
    customer_prueba = Customers("Nintendo", "Adolfo", "Engineer", "Coop Abogados", "Arequipa",
                                 "Arequipa", 4329, "Perú", 965734852, 2436157)
    
    adolf = Employees("Paredes", "Adolfo", "Engineer", "Sistems", "03/12/2008", " 01/01/2026", "Coop.Lawyers", 
                      "Arequipa", "Arequipa", "1242", "Perú", "243534534", "+51", "None", "Link.photo", "None")

    order1 = Order(customer_prueba.get_customer_id(), adolf.get_employee_id(), "23-10-2022", "31- 12- 2023", "31-12-2024", "Ship via", "freight", "ship name", "ship adress", "ship city", "ship region", 4234, "Perú")
    print(order1)                         

        
      