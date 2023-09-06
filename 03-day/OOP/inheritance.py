class Category:
    def __init__(self, name:str) -> None:
        self.name = name

    def get_info(self):
        return f'Category name: {self.name}'
    

class SubCategory(Category):
    def __init__(self, category_name, subcategory_name) -> None:
        super().__init__(category_name)
        self.subcategory_name = subcategory_name


subcat = SubCategory('VGA', 'AMD')
print(subcat.name)
print(subcat.subcategory_name)
print(subcat.get_info())
