import sys
sys.path.insert(0, "..")
from src.cashier import Cashier

def test_serve_customer():
    c = Cashier("Test")
    earned, tip = c.serve_customer(10.0)
    assert earned >= 10.0
    assert tip >= 0
    assert c.customers_served == 1
    assert c.total_earned >= 10.0

def test_reset():
    c = Cashier("Test")
    c.serve_customer(5.0)
    c.reset()
    assert c.customers_served == 0
    assert c.total_earned == 0