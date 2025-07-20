# app.py

import streamlit as st
from destination_agent import destination_agent
from booking_agent import booking_agent
from explore_agent import explore_agent

st.set_page_config(page_title="AI Travel Designer", layout="centered")

st.title("✈️ AI Travel Designer Agent")

# Travel type selection
travel_type = st.radio(
    "Do you want a domestic or international trip?",
    ("domestic", "international")
)

# User mood
user_mood = st.selectbox(
    "What's your mood for this trip?",
    ["relaxation", "adventure", "culture"]
)

# Get destination options
destinations = destination_agent(user_mood, travel_type)

destination = st.selectbox(
    "Select a destination:",
    destinations
)

from_city = st.text_input("Enter your departure city (e.g. Lahore, Karachi):")

if st.button("Search Trip"):
    if not from_city:
        st.warning("Please enter your departure city.")
    else:
        booking_info = booking_agent(destination, from_city, travel_type)
        
        st.subheader("✈️ Flight Options")
        flights = booking_info["flights"]["flights"]
        if flights:
            for flight in flights:
                st.write(f"**From**: {flight['from']}")
                st.write(f"**To**: {flight['to']}")
                st.write(f"**Price**: Rs. {flight['price']}")
                st.write(f"**Airline**: {flight['airline']}")
                st.write(f"**Departure**: {flight['departure']}")
                st.markdown("---")
        else:
            st.write("No flights found.")

        st.subheader("🏨 Hotel Options")
        hotels = booking_info["hotels"]["hotels"]
        if hotels:
            for hotel in hotels:
                st.write(f"**Hotel**: {hotel['name']}")
                st.write(f"**Price/Night**: Rs. {hotel['price_per_night']}")
                st.write(f"**Rating**: {hotel['rating']}")
                st.markdown("---")
        else:
            st.write("No hotels found.")

        st.subheader(f"🎯 Top Things To Do in {destination}")
        activities = explore_agent(destination)
        for act in activities:
            st.write(f"• {act}")
