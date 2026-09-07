from dataclasses import dataclass


@dataclass(frozen=True)
class OriginCartageData:
    currency: str = "INR - Indian Rupee"
    density: int = 167
    departure_terminal: str = "T1"
    start_date: str = "2026-09-05"
    end_date: str = "2026-09-06"
    fuel_surcharge: int = 10
    notification: int = 5
    city: str = "chennai"
    from_postcode: str = "600002"
    to_postcode: str = "600005"
    toll_fee: int = 100
    toll_fee_unit: str = "per shipment"
    booking_deadline: str = "09:00"
    timeline: int = 5
    base_rate: int = 50
    minimum_rate: int = 40
    rate_per_kg: int = 5
    charge_type: str = "Chargeable"
    document_name: str = "Raju"


ORIGIN_CARTAGE_DATA = OriginCartageData()
