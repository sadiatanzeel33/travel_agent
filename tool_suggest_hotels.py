
def suggest_hotels(destination, travel_type):
    hotels = {
        # Domestic
        "Murree": [
            {"name": "Pearl Continental Bhurban", "price_per_night": 18000, "rating": 4.5},
            {"name": "Shangrila Resort", "price_per_night": 15000, "rating": 4.2}
        ],
        "Hunza": [
            {"name": "Serena Hunza", "price_per_night": 22000, "rating": 4.6},
            {"name": "Eagles Nest Hotel", "price_per_night": 16000, "rating": 4.3}
        ],
        # International
        "Maldives": [
            {"name": "Conrad Maldives", "price_per_night": 180000, "rating": 4.8},
            {"name": "Soneva Jani", "price_per_night": 250000, "rating": 5.0}
        ],
        "Italy": [
            {"name": "Hotel Bernini Palace", "price_per_night": 120000, "rating": 4.6},
            {"name": "Grand Hotel Vesuvio", "price_per_night": 140000, "rating": 4.7}
        ]
    }

    return {"hotels": hotels.get(destination, [])}
