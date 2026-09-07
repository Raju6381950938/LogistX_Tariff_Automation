import random

def get_currency():
    return random.choice([
        "INR - Indian Rupee",
        "USD - US Dollar",
        "EUR - Euro",
        "AUD - Australian Dollar"
    ])

def get_density():
    return random.randint(100, 500)

def get_terminal():
    return random.choice([
        "T1",
        "T2",
        "T3",
        "T4"
    ])

def get_start_date():
    return random.choice([
        "2026-09-07",
        "2026-09-08",
        "2026-09-10",
    ])

def get_end_date():
    return random.choice([
        "2026-09-26",
        "2026-09-27",
        "2026-09-28",
    ])











