import streamlit as st
import requests

# Set your API Key here (Replace with your own OpenWeatherMap API Key)
API_KEY = "91c311ca23c9845b349fe3d78a317d63"

# Function to fetch weather data
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI
st.title("🌍 Real-Time Weather Analysis System")

# User input for city name
city = st.text_input("Enter city name:", "")

if st.button("Get Weather"):
    if not city.strip():
        st.error("⚠️ Please enter a city name!")
    else:
        data = get_weather(city)
        if data:
            st.subheader(f"📍 Weather in {city.title()}")
            st.write(f"🌡️ **Temperature:** {data['main']['temp']}°C")
            st.write(f"💧 **Humidity:** {data['main']['humidity']}%")
            st.write(f"🌬️ **Wind Speed:** {data['wind']['speed']} m/s")
            st.write(f"⚖️ **Pressure:** {data['main']['pressure']} hPa")
            st.write(f"☁️ **Condition:** {data['weather'][0]['description'].title()}")

            st.success("✅ Weather data fetched successfully!")
        else:
            st.error(f"❌ Could not fetch weather data for '{city}'. Please check the city name.")
