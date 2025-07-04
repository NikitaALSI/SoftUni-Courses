class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return list(filter(lambda x: x.startswith(first_letter), self.products))

    def __repr__(self):
        text = f"Items in the {self.name} catalogue:"
        for prod in sorted(self.products):
            text += "\n"+prod
        return text

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)



