class Employees:
    id_employees = 0

    # Constructor de clase
    def __init__(self, last_name, first_name, title, title_of_courtesy, birth_date, hire_date,
     adrees, city, region, postal_code, country, home_phone, extension, notes, photo, reports_to):
        Employees.id_employees += 1
        self._id = Employees.id_employees
        self._last_name = last_name
        self._first_name = first_name
        self._title = title
        self._title_of_courtesy = title_of_courtesy 
        self._birth_date = birth_date
        self._hire_date = hire_date
        self._adress = adrees 
        self._city = city
        self._region = region
        self._postal_code = postal_code
        self._country = country
        self._home_phone = home_phone
        self._extension = extension
        self._notes = notes
        self._photo = photo
        self._reports_to = reports_to
    # ---Fin constructor de clase---

    # ---Métodos get---
    def get_last_name(self):
        return self._last_name
    
    def get_first_name(self):
        return self._first_name
    
    def get_title(self):
        return self._title
    
    def get_title_of_Courtesy(self):
        return self._title_of_courtesy

    def get_birth_date(self):
        return self._birth_date
    
    def get_hire_date(self):
        return self._hire_date
    
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
    
    def get_home_phone(self):
        return self._home_phone
    
    def get_extension(self):
        return self._extension
    
    def get_notes(self):
        return self._notes
    
    def get_photo(self):
        return self._photo
    
    def get_reports_to(self):
        return self._reports_to
    # ---Fin métodos get---

    # ---Métodos set---
    def set_last_name(self, last_name):
        self._last_name = last_name
    
    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def set_title(self, title):
        self._title = title
    
    def set_title_of_Courtesy(self, title_of_courtesy):
        self._title_of_courtesy = title_of_courtesy

    def set_birth_date(self, birth_date):
        self._birth_date = birth_date
    
    def set_hire_date(self,hire_date):
        self._hire_date = hire_date
    
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
    
    def set_home_phone(self, home_phone):
        self._home_phone = home_phone
    
    def set_extension(self, extension):
        self._extension = extension
    
    def set_notes(self,notes):
        self._notes = notes
    
    def set_photo(self,photo):
        self._photo = photo
    
    def set_reports_to(self,reports_to):
        self._reports_to = reports_to
    # ---Fin métodos set--

    # ---Método string---
    def __str__(self):
        return f"""
        Empleado N{self._id}
            Last name: {self._last_name}
            Fist name: {self._first_name}
            Title: {self._title}
            Title of courtesy: {self._title_of_courtesy}
            Birth date: {self._birth_date}
            Hire date: {self._hire_date}
            Adress: {self._adress}
            City: {self._city}
            Region: {self._region}
            Postal code: {self._postal_code}
            Country: {self._country}
            Home phone:{self._home_phone}
            Extension: {self._extension}
            Notes: {self._extension}
            Photo: {self._notes}
            Reports to: {self._reports_to}
        """

if __name__ == "__main__":
    adolf = Employees("Paredes", "Adolfo", "Engineer", "Sistems", "03/12/2008", " 01/01/2026", "Coop.Lawyers", 
                      "Arequipa", "Arequipa", "1242", "Perú", "243534534", "+51", "None", "Link.photo", "None")
    print(adolf)