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
        "Anna International Airport",
        "Kamaraj Domestic Airport",
    ])

def get_terminal_postcode():
    return random.choice([
        "600020",
        "600030",
        "600040",
    ])

def get_terminal_name_another():
    return random.choice([
        "T1",
        "T2",
        "T3",
    ])

def get_terminal_address_another():
    return random.choice([
        "Meenambakkam Airport",
        "Greenfield International Airport"
    ])

def get_terminal_postcode_another():
    return random.choice([
        "600020",
        "600030",
        "600040",
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

def get_Export_Documents():
    return random.randint(10, 50)

def get_UOM():
    return random.choice([
        "kilogram",
        "shipment",
    ])

def get_basis():
    return random.choice([
        "Chargeable",
        "Actual",
    ])

def get_Origin_Customs():
    return random.randint(10, 50)

def get_CMR_Fee():
    return random.randint(10, 80)

def get_Export_Licence_Fee():
    return random.randint(50, 80)

def get_CISS_Fee():
    return random.randint(10, 60)

def get_Origin_Carrier_Fee():
    return random.randint(15, 50)

def get_FOB_Tax():
    return random.randint(100, 500)

def get_fee_name():
    return random.choice([
        "Customs Duty",
        "Sales Tax",
        "Property Tax",
    ])

def get_rate():
    return random.randint(30, 60)

def get_fixed_rate_unit():
    return random.choice([
         "40'-G1",
         "VAN",
         "TRUCK",
         "20'-G1",
    ])

def get_rate():
    return random.randint(10, 60)



