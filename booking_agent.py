

from tool_get_flights import get_flights
from tool_suggest_hotels import suggest_hotels

def booking_agent(destination, from_city, travel_type):
    flights = get_flights(destination, from_city, travel_type)
    hotels = suggest_hotels(destination, travel_type)

    return {
        "flights": flights,
        "hotels": hotels
    }
