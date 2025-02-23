import streamlit as st
import requests

# Set page title and layout
st.set_page_config(page_title="Weather App", layout="centered")

# Custom CSS for modern UI
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .title {
        font-size: 38px;
        font-weight: bold;
        text-align: center;
        color: #ffcc00;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #bbb;
    }
    .info-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #222;
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
        text-align: center;
    }
    .emoji {
        font-size: 50px;
    }
    .weather-details {
        font-size: 20px;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# API Key for OpenWeatherMap (Replace with your API key)
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
    data = response.json()
    
    if response.status_code == 200:
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "country": data["sys"]["country"]
        }
    else:
        return None

# Function to suggest outfit based on temperature
def suggest_outfit(temp):
    if temp < 10:
        return "🧥 Wear a heavy jacket and stay warm!"
    elif temp < 20:
        return "🧣 A sweater or hoodie should be good!"
    elif temp < 30:
        return "👕 Light clothes will keep you comfortable!"
    else:
        return "🩳 It's hot! Wear shorts and stay hydrated!"

# Streamlit UI Elements
st.markdown('<div class="title">🌍 Real-Time Weather Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🔍 Get temperature, humidity, and weather conditions instantly!</div>', unsafe_allow_html=True)

# Input for city name
city = st.text_input("Enter city name 🌆", placeholder="E.g., Pune, Mumbai, New York", help="Type a city name and press Enter")

# Button to check weather
if st.button("🔍 Check Weather"):
    if city:
        weather = get_weather(city)
        if weather:
            emoji = "☀️" if "clear" in weather["weather"] else "⛅" if "cloud" in weather["weather"] else "🌧️" if "rain" in weather["weather"] else "❄️"
            outfit_suggestion = suggest_outfit(weather["temperature"])

            st.markdown(f"""
                <div class='info-box'>
                    <div class="emoji">{emoji}</div>
                    <h3>📍 {city}, {weather["country"]}</h3>
                    <p class="weather-details">🌡️ Temperature: {weather["temperature"]}°C</p>
                    <p class="weather-details">💧 Humidity: {weather["humidity"]}%</p>
                    <p class="weather-details">🌪️ Wind Speed: {weather["wind_speed"]} m/s</p>
                    <p class="weather-details">🌤️ Condition: {weather["weather"].capitalize()}</p>
                    <hr>
                    <p class="weather-details">{outfit_suggestion}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Could not fetch weather data. Please check the city name or try again later.")
    else:
        st.warning("⚠️ Please enter a city name!")

