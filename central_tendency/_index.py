from ._registry import OPERATIONS

class Series:
    def __init__(self, data):
        if not data:
            raise ValueError("Empty dataset")
        self.data = data

    def compute(self, name):
        if name not in OPERATIONS:
            raise ValueError(f"Unknown operation '{name}'")
        return OPERATIONS[name](self.data)

    def available(self):
        return list(OPERATIONS.keys())
