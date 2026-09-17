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

def get_terminal_name():
    return random.choice([
        "T1",
        "T2",
        "T3",
    ])

def get_terminal_address():
    return random.choice([
        "Meenambakkam",
        "Domestic",
        "International"
    ])

def get_terminal_postcode():
    return random.choice([
        "600020",
        "600030",
        "600040",
    ])

def get_arrival_name():
    return random.choice([
        "P1",
        "P2",
        "P3",
    ])

def get_arrival_address():
    return random.choice([
        "Domestic",
        "International",
    ])

def get_arrival_postcode():
    return random.choice([
        "6000",
        "6001",
        "6002",
    ])

def get_start_date():
    return random.choice([
        "2026-09-20",
        "2026-09-21",
        "2026-09-22",
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
   








