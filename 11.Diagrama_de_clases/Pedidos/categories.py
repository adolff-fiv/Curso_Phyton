class Categories:
    id_categories = 0

    # Constructor de clase
    def __init__(self, category_name, description, picture):
        Categories.id_categories += 1
        self._id = Categories.id_categories
        self._category_name = category_name
        self._description = description
        self._picture = picture
    # ---Fin constructor de clase---

    # ---Métodos set---
    def set_category_name(self, category_name):
        self._category_name = category_name
    
    def set_description(self, description):
        self._description = description

    def set_picture(self, picture):
        self._picture = picture
    # ---Fin métodos set---

    # ---Métodos get---
    def get_category_id(self):
        return self.id_categories
    
    def get_category_name(self):
        return self._category_name
    
    def get_description(self):
        return self._description
    
    def get_picture(self):
        return self._picture
    # ---Fin métodos get---

    # ---Método string---
    def __str__(self):
        return f"""
        Category N{self._id}
            Category name: {self._category_name}
            Description: {self._description}
            Picture: {self._picture}
        """
    
if __name__ == "__main__":
    category1 = Categories("Nintendo games", "Too many", "Nintendo.jpg")
    print(category1)