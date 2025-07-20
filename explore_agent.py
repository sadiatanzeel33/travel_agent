

def explore_agent(destination):
    attractions = {
        # Domestic
        "Murree": ["Chair Lift Patriata", "Mall Road", "Pindi Point"],
        "Hunza": ["Altit Fort", "Baltit Fort", "Attabad Lake"],
        "Skardu": ["Shangrila Lake", "Deosai Plains", "Cold Desert"],
        "Lahore": ["Badshahi Mosque", "Lahore Fort", "Food Street"],
        # International
        "Maldives": ["Snorkeling", "Underwater dining"],
        "Italy": ["Vatican Museums", "Eat authentic pasta"],
        "Japan": ["Visit Kyoto temples", "Try sushi in Tokyo"]
    }

    return attractions.get(destination, ["Explore local sights", "Try local food"])
