import time
from src import AutoFryer, Cashier, Menu

def main():
    print("Restaurant Tycoon 2 Enhancer - Starting simulation...")
    menu = Menu()
    fryer = AutoFryer(3)
    cashier = Cashier("Alex")

    # Add a custom item
    menu.add_item("Hot Dog", 3.49)

    print("Menu:", menu.list_menu())

    # Start cooking
    fryer.start_cooking("Fries")
    fryer.start_cooking("Burger")
    print("Fryer status:", fryer.status())

    # Simulate time passing
    for _ in range(5):
        fryer.tick(20)
        time.sleep(0.1)

    # Collect done items
    done = fryer.collect_done()
    print("Collected from fryer:", done)

    # Serve a customer
    earned, tip = cashier.serve_customer(menu.get_price("Burger"))
    print(f"Served customer: earned ${earned:.2f} (tip ${tip:.2f})")

    print("Cashier stats:", cashier)

if __name__ == "__main__":
    main()