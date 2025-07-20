

def get_flights(destination, from_city, travel_type):
    if travel_type == "domestic":
        return {
            "flights": [
                {
                    "from": from_city,
                    "to": destination,
                    "price": 12000,
                    "airline": "PIA",
                    "departure": "2025-08-10"
                }
            ]
        }
    else:
        return {
            "flights": [
                {
                    "from": from_city,
                    "to": destination,
                    "price": 150000,
                    "airline": "Emirates",
                    "departure": "2025-09-15"
                }
            ]
        }
