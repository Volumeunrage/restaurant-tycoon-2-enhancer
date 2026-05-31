class Menu:
    def __init__(self):
        self.items = {
            "Burger": 5.99,
            "Fries": 2.49,
            "Soda": 1.99,
            "Pizza": 8.99,
            "Salad": 4.49,
        }

    def get_price(self, item):
        return self.items.get(item, None)

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        return self.items.pop(name, None)

    def list_menu(self):
        return list(self.items.items())

    def __len__(self):
        return len(self.items)