
def destination_agent(user_mood, travel_type):
    domestic_destinations = {
        "relaxation": ["Murree", "Hunza", "Skardu"],
        "adventure": ["Swat", "Naran Kaghan", "Skardu"],
        "culture": ["Lahore", "Multan", "Karachi"]
    }

    international_destinations = {
        "relaxation": ["Maldives", "Bali", "Santorini"],
        "adventure": ["Nepal", "New Zealand", "Peru"],
        "culture": ["Italy", "Japan", "Egypt"]
    }

    if travel_type == "domestic":
        return domestic_destinations.get(user_mood.lower(), ["Islamabad", "Gwadar", "Murree"])
    else:
        return international_destinations.get(user_mood.lower(), ["Spain", "Thailand", "Portugal"])
