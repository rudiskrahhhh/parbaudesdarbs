class Item():
    def __init__(self, title, category, quantity, price):
        self.title = title
        self.quantity = quantity
        self.category = category
        self.price = price

    def change_title(self, new_title):
        self.title = new_title

    def sell_item(self):
        self.quantity = int(self.quantity)
        self.quantity -= 1

    def update_category(self, new_category=""):
        if new_category == "":
            if self.category == "aparats":
                self.category = "lieta"
            else:
                self.category = "lieta"
        else:
            self.category = new_category
        self.show_info()

    def show_info(self):
        if self.category == "lieta":
            category_name = "lieta"
        elif self.category == "aparats":
            category_name = "aparats"
        else:
            category_name = self.category
        return f"nosaukums: {self.title}\n kategorija: {category_name}\n daudzums: {self.quantity}\n cena: {self.price}€"
