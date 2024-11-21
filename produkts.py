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
            if self.category == "Gadget":
                self.category = "Accessory"
            else:
                self.category = "Accessory"
        else:
            self.category = new_category
        self.show_info()

    def show_info(self):
        if self.category == "Accessory":
            category_name = "Accessory"
        elif self.category == "Gadget":
            category_name = "Gadget"
        else:
            category_name = self.category
        return f"Item Title: {self.title}\n Category: {category_name}\n Total Quantity: {self.quantity}\n Price: {self.price}€"
