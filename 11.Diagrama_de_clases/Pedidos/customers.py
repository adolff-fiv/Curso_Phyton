class Customers:
    id_customers = 0

    # Constructor de clase
    def __init__(self, company_name, contact_name, contact_title,  
     adress, city, region, postal_code, country, phone, fax):
        Customers.id_customers += 1
        self._id = Customers.id_customers
        self._company_name = company_name
        self._contact_name = contact_name
        self._contact_title = contact_title
        self._adress = adress 
        self._city = city
        self._region = region
        self._postal_code = postal_code
        self._country = country
        self._phone = phone
        self._fax = fax
    # ---Fin constructor de clase---

    # ---Métodos set---
    def set_company_name(self, company_name):
        self._company_name = company_name
    
    def set_contact_name(self, contact_name):
        self._contact_name = contact_name
    
    def set_contact_title(self, contact_title):
        self._contact_title = contact_title
    
    def set_adress(self, adress):
        self._adress = adress
    
    def set_city(self,city):
        self._city = city
    
    def set_region(self,region):
        self._region = region
    
    def set_postal_code(self,postal_code):
        self._postal_code = postal_code
    
    def set_country(self, country):
        self.country = country
    
    def set_phone(self, phone):
        self._phone = phone
    
    def set_fax(self, fax):
        self._fax = fax
    # ---Fin métodos set---

    # ---Métodos get---
    def get_company_name(self):
        return self._company_name
    
    def get_company_name(self):
        return self._company_name
    
    def get_contact_title(self):
        return self._contact_title
    
    def get_adress(self):
        return self._adress
    
    def get_city(self):
        return self._city
    
    def get_region(self):
        return self._region
    
    def get_postal_code(self):
        return self._postal_code
    
    def get_country(self):
        return self._country
    
    def get_phone(self):
        return self._phone
    
    def get_fax(self):
        return self._fax
    # ---Fin métodos get--

    # ---Método string---
    def __str__(self):
        return f"""
        Customer N{self._id}
            Company name: {self._company_name}
            Contact name: {self._contact_name}
            Contact title: {self._contact_title}
            Adress: {self._adress}
            City: {self._city}
            Region: {self._region}
            Postal code: {self._postal_code}
            Country: {self._country}
            Fax: {self._fax}
        """
    
if __name__ == "__main__":
    customer_prueba = Customers("Nintendo", "Adolfo", "Engineer", "Coop Abogados", "Arequipa",
                                 "Arequipa", 4329, "Perú", 965734852, 2436157)
    print(customer_prueba)