from produkts import Item

class Computer(Item):
    def __init__(self, title, quantity, manufacturer):
        super().__init__(title, quantity, "Gadget")
        self.manufacturer = manufacturer
        self.show_info()

    def show_info(self):
        super().show_info()
