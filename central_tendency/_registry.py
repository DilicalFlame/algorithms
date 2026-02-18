OPERATIONS = {}

def register(func):
    if func.__name__ in OPERATIONS:
        raise ValueError(f"Operation '{func.__name__}' already registered")
    OPERATIONS[func.__name__] = func
