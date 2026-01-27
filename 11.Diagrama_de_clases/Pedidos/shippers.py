class Shippers:
    id_shipper = 0

    # Constructor de clase
    def __init__(self, company_name, phone,):
        Shippers.id_shipper += 1
        self._id = Shippers.id_shipper
        self._company_name = company_name
        self._phone = phone
    # ---Fin constructor de clase---

    # ---Métodos set---
    def set_company_name(self, company_name):
        self._company_name = company_name
    
    def set_phone(self, phone):
        self._phone = phone


    # ---Fin métodos set---

    # ---Métodos get---
    def get_company_name(self):
        return self._company_name
    
    def get_phone(self):
        return self._phone
    
    # ---Fin métodos get---

    # ---Método string---
    def __str__(self):
        return f"""
    Shipper N{self._id}
            Company name: {self._company_name}
            Phone: {self._phone}
        """
    
if __name__ == "__main__":
    Shipper = Shippers("Nintendo games", 948578243)
    print(Shipper)