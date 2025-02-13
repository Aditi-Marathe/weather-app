import streamlit as st
import requests

# Function to get weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI
st.title("🌤️ Weather Checker for Multiple Cities")

# User input for API key and cities
api_key = st.text_input("Enter your OpenWeatherMap API Key:", type="password")
cities = st.text_area("Enter city names (one per line):").split("\n")

if st.button("Check Weather"):
    if not api_key:
        st.error("Please enter a valid API key.")
    elif not cities:
        st.error("Please enter at least one city.")
    else:
        for city in cities:
            city = city.strip()
            if city:
                data = get_weather(city, api_key)
                if data:
                    st.subheader(f"Weather in {city}")
                    st.write(f"🌡️ Temperature: {data['main']['temp']}°C")
                    st.write(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
                    st.write(f"☁️ Condition: {data['weather'][0]['description'].title()}")
                    st.write("---")
                else:
                    st.error(f"Could not fetch weather for {city}. Check the city name or API key.")

