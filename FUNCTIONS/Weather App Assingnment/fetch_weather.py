# weather_app/fetch_weather.py

def get_current_weather(city):
    weather_data = {
        "New York": {"temperature": 25, "condition": "Sunny"},
        "London": {"temperature": 15, "condition": "Cloudy"},
        "Mumbai": {"temperature": 30, "condition": "Rainy"},
    }
    return weather_data.get(city, {"temperature": "N/A", "condition": "N/A"})
