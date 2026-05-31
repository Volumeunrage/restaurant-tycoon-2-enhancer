import random

class Cashier:
    def __init__(self, name="Default"):
        self.name = name
        self.total_earned = 0
        self.customers_served = 0

    def serve_customer(self, order_total):
        tip = round(random.uniform(0, 2.5), 2)
        earned = order_total + tip
        self.total_earned += earned
        self.customers_served += 1
        return earned, tip

    def reset(self):
        self.total_earned = 0
        self.customers_served = 0

    def __repr__(self):
        return f"Cashier({self.name}, served={self.customers_served}, earned=${self.total_earned:.2f})"