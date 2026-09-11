import random

def get_currency():
    return random.choice([
        "INR - Indian Rupee",
        "USD - US Dollar",
        "EUR - Euro",
        "AUD - Australian Dollar"
    ])

def get_density():
    return random.randint(10, 50)

def get_terminal():
    return random.choice([
        "T1",
        "T2",
    ])

def get_unpacking():
    return random.choice([
        "PER",
    ])

def get_arrival():
    return random.choice([
        "T3",
        "T4",
    ])

def get_start_date():
    return random.choice([
        "2026-09-11",
        "2026-09-12",
        "2026-09-13",
    ])

def get_end_date():
    return random.choice([
        "2026-09-26",
        "2026-09-27",
        "2026-09-28",
    ])

def get_terminal_fee():
    return random.randint(10, 50)

def get_UOM():
    return random.choice([
        "kilogram",
        "shipment",
        "tonne"
    ])

def get_basis():
    return random.choice([
        "Chargeable",
        "Actual",
    ])

def get_terminal_minimum():
    return random.randint(10, 50)

def get_UOM():
    return random.choice([
        "kilogram",
        "tonne"
    ])

def get_basis():
    return random.choice([
        "Chargeable",
        "Actual",
    ])

def get_fee():
    return random.choice([
        "Airline Terminal Fee",
        "Processing Charge",
        "Terminal Storage Fee",
    ])

def get_rate():
    return random.randint(30, 60)

def get_base_rate():
    return random.randint(200, 600)

def get_minimum():
    return random.randint(300, 400)

def get_condition():
    return random.choice([
        "Less than <",
        "Greater than >",
    ])

def get_weight():
    return random.randint(5, 10)

def get_per_kg():
    return random.randint(10, 20)

def get_fuel_surcharge():
    return random.randint(30, 40)

def get_UOM():
    return random.choice([
        "kilogram",
        "tonne"
    ])

def get_basis():
    return random.choice([
        "Chargeable",
        "Actual",
    ])

def get_notification():
    return random.randint(1, 10)

def get_carrier():
    return random.choice([
        "Air_india",
        "austrian",
        "cargolux",
    ])

def get_transit_days():
    return random.randint(1, 10)
   








