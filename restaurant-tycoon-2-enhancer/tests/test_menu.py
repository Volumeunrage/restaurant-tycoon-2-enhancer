import sys
sys.path.insert(0, "..")
from src.menu import Menu

def test_get_price():
    m = Menu()
    assert m.get_price("Burger") == 5.99
    assert m.get_price("Nonexistent") is None

def test_add_and_remove():
    m = Menu()
    m.add_item("Taco", 2.99)
    assert m.get_price("Taco") == 2.99
    m.remove_item("Taco")
    assert m.get_price("Taco") is None

def test_list_menu():
    m = Menu()
    items = m.list_menu()
    assert ("Burger", 5.99) in items
    assert len(items) == 5