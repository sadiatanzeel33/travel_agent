

from destination_agent import destination_agent
from booking_agent import booking_agent
from explore_agent import explore_agent

def run_travel_designer():
    # Domestic or International?
    travel_type = input("Do you want a domestic or international trip? ").strip().lower()
    if travel_type not in ["domestic", "international"]:
        print("Invalid choice. Exiting.")
        return

    user_mood = input("How do you feel? (relaxation/adventure/culture): ").strip().lower()

    # Get destinations
    options = destination_agent(user_mood, travel_type)
    print("\nSuggested destinations:")
    for idx, dest in enumerate(options, start=1):
        print(f"{idx}. {dest}")

    choice = int(input("\nSelect a destination number: "))
    destination = options[choice - 1]

    from_city = input("Enter your departure city: ").strip()

    # Get flights & hotels
    booking_info = booking_agent(destination, from_city, travel_type)

    print("\nFlight Options:")
    for flight in booking_info["flights"]["flights"]:
        print(f"- From {flight['from']} to {flight['to']} at Rs.{flight['price']} via {flight['airline']} on {flight['departure']}")

    print("\nHotel Options:")
    hotels = booking_info["hotels"]["hotels"]
    if hotels:
        for hotel in hotels:
            print(f"- {hotel['name']} → Rs.{hotel['price_per_night']} per night (Rating: {hotel['rating']})")
    else:
        print("No hotels found for this destination.")

    # Get exploration options
    activities = explore_agent(destination)
    print(f"\nTop experiences in {destination}:")
    for act in activities:
        print(f"- {act}")

if __name__ == "__main__":
    run_travel_designer()
