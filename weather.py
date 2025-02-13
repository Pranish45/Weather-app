import streamlit as st
import requests
from PIL import Image
import io

# Function to get weather data from OpenWeatherMap API
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # For Celsius
    
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        temp = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = weather['description']
        wind_speed = wind['speed']
        icon = weather['icon']
        
        return {
            'temp': temp,
            'pressure': pressure,
            'humidity': humidity,
            'weather_description': weather_description,
            'wind_speed': wind_speed,
            'icon': icon
        }
    else:
        return None  # If the city is not found or API error occurs

# Streamlit UI
def main():
    # Set the page title and theme
    st.set_page_config(page_title="Weather App", page_icon=":sunny:", layout="centered")
    st.title("🌦️ Weather App 🌦️")
    
    # Add some spacing for aesthetics
    st.markdown("<br>", unsafe_allow_html=True)
    
    # API Key (keep it secure in real-world applications)
    api_key = "a0b539b5b0a9bcec8e37933a569d13f6"  # Replace with your OpenWeatherMap API key
    
    # User input for city name
    city = st.text_input("Enter city name", "").capitalize()
    
    # Make the app more interactive by displaying a button
    if st.button("Get Weather"):
        if city:
            # Get the weather data
            weather_data = get_weather(city, api_key)

            if weather_data:
                # Displaying weather data in a formatted layout
                st.subheader(f"Weather in {city}:")
                
                # Displaying weather icon
                icon_url = f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
                st.image(icon_url, width=100)
                
                # Display temperature with a creative font
                st.markdown(f"**Temperature:** {weather_data['temp']}°C")
                st.markdown(f"**Pressure:** {weather_data['pressure']} hPa")
                st.markdown(f"**Humidity:** {weather_data['humidity']}%")
                st.markdown(f"**Weather Description:** {weather_data['weather_description'].capitalize()}")
                st.markdown(f"**Wind Speed:** {weather_data['wind_speed']} m/s")
                
                # Add a fun, weather-themed background image based on the weather
                if "clear" in weather_data['weather_description']:
                    st.markdown('<style>body{background-color: #ffcc00;}</style>', unsafe_allow_html=True)
                elif "rain" in weather_data['weather_description']:
                    st.markdown('<style>body{background-color: #0077be;}</style>', unsafe_allow_html=True)
                elif "cloud" in weather_data['weather_description']:
                    st.markdown('<style>body{background-color: #c0c0c0;}</style>', unsafe_allow_html=True)
                else:
                    st.markdown('<style>body{background-color: #ff6347;}</style>', unsafe_allow_html=True)
                
            else:
                st.error("City not found or invalid API key!")
        else:
            st.warning("Please enter a city name to get weather data.")
    
    # Add footer with your name or any additional details
    st.markdown("""
        <hr>
        <p style="text-align: center; font-size: 16px;">Made with ❤️ by Pranish</p>
        """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
