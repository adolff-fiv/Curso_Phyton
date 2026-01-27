from order_details import Order_Details
from order import Order
from supliers import Suplier
from categories import Categories
from products import Product
from customers import Customers
from employees import Employees

# --- Creating customer ---
customer_prueba = Customers("Nintendo", "Adolfo", "Engineer", "Coop Abogados", "Arequipa",
                                 "Arequipa", 4329, "Perú", 965734852, 2436157)

# --- Creating employer ---
adolf = Employees("Paredes", "Adolfo", "Engineer", "Sistems", "03/12/2008", " 01/01/2026", "Coop.Lawyers", 
                      "Arequipa", "Arequipa", "1242", "Perú", "243534534", "+51", "None", "Link.photo", "None")

# --- Creating order ---
order1 = Order(customer_prueba.get_customer_id(), adolf.get_employee_id(), "23-10-2022", 
                   "31- 12- 2023", "31-12-2024", "Ship via", "freight", "ship name", 
                   "ship adress", "ship city", "ship region", 4234, "Perú")
# --- Creating supplier ---
suplier_prueba = Suplier("Nintendo", "Adolfo", "Engineer", "Coop Abogados", "Arequipa",
                                 "Arequipa", 4329, "Perú", 965734852, 2436157, 2)

# --- Creating categories ---
category1 = Categories("Nintendo games", "Too many", "Nintendo.jpg")
category2 = Categories("XBOX games", "The best", "XBOX.jpg")

# --- Creating products ---
product1 = Product("Computadoras", suplier_prueba.get_suplier_id(), category1.get_category_id(), 12, 5, 11, 6, 
                       "Reorder_level", False)
product2 = Product("laptops", suplier_prueba.get_suplier_id(), category2.get_category_id(), 142, 8, 31, 60, 
                       "Reorder_level", False)

# --- Creating order detail ---
order_detail1 = Order_Details(order1.get_order_id(), [product1.get_product_name(), product2.get_product_name()], 
                              20, 30, False)
print(order_detail1)