import time
import random

class AutoFryer:
    def __init__(self, slot_count=4):
        self.slot_count = slot_count
        self.fryers = [{"food": None, "progress": 0} for _ in range(slot_count)]

    def start_cooking(self, food_item):
        for slot in self.fryers:
            if slot["food"] is None:
                slot["food"] = food_item
                slot["progress"] = 0
                return True
        return False

    def tick(self, amount=5):
        for slot in self.fryers:
            if slot["food"] is not None:
                slot["progress"] += amount
                if slot["progress"] >= 100:
                    slot["progress"] = 100

    def collect_done(self):
        collected = []
        for slot in self.fryers:
            if slot["food"] is not None and slot["progress"] >= 100:
                collected.append(slot["food"])
                slot["food"] = None
                slot["progress"] = 0
        return collected

    def status(self):
        return [f"{s['food'] or 'empty'} ({s['progress']}%)" for s in self.fryers]