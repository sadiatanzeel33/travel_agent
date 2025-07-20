
🧳 AI Travel Designer Agent
An intelligent travel planning agent that crafts personalized travel experiences by coordinating between modular AI agents.

🧠 Features
Personalized Destination Suggestions
Recommends travel destinations based on user's mood or interests using the DestinationAgent.

Flight & Hotel Booking (Simulated)
Simulates booking via BookingAgent using tools like get_flights() and suggest_hotels() with mock data.

Explore Recommendations
ExploreAgent suggests local attractions, restaurants, and activities tailored to your chosen destination.

⚙️ Tech Stack
OpenAI Agent SDK with RunnableAgent

Modular Agents for task-specific delegation

Tools: Travel Info Generator, Hotel Picker (mock data)

🔄 Agent Handoff Workflow
DestinationAgent → BookingAgent → ExploreAgent

🧩 Designed for easy extensibility with real APIs or custom travel datasets in production.    
