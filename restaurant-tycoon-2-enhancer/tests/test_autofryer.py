import sys
sys.path.insert(0, "..")
from src.autofryer import AutoFryer

def test_start_cooking():
    fryer = AutoFryer(2)
    assert fryer.start_cooking("Fries") == True
    assert fryer.start_cooking("Burger") == True
    assert fryer.start_cooking("Pizza") == False  # no slots

def test_tick_and_collect():
    fryer = AutoFryer(1)
    fryer.start_cooking("Fries")
    fryer.tick(50)
    assert fryer.status()[0] == "Fries (50%)"
    fryer.tick(50)
    collected = fryer.collect_done()
    assert collected == ["Fries"]
    assert fryer.status()[0] == "empty (0%)"

def test_empty_collect():
    fryer = AutoFryer(2)
    assert fryer.collect_done() == []