import streamlit as st
import requests
from datetime import datetime

# Function to get weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
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
            'icon': icon,
            'sunrise': datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
            'sunset': datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
        }
    return None

# Function to load a default image if no background image is found
def load_default_image():
    # URL of a default background image
    return "https://example.com/default_background_image.jpg"  # Replace with a real default image URL

# Streamlit UI
def main():
    st.set_page_config(page_title="Weather App", page_icon=":sunny:", layout="centered")
    st.title("🌦️ Weather App 🌦️")
    
    # API Keys
    weather_api_key = "a0b539b5b0a9bcec8e37933a569d13f6"  # Replace with your OpenWeatherMap API key
    
    # Add some spacing for aesthetics
    st.markdown("<br>", unsafe_allow_html=True)
    
    # User input for city name
    city = st.text_input("Enter city name", "").capitalize()

    # Check if the user has entered a city
    if city:
        # Fetch the weather data
        weather_data = get_weather(city, weather_api_key)

        # Display background image (default image in this case)
        default_image_url = load_default_image()
        st.image(default_image_url, use_column_width=True)

        if weather_data:
            st.subheader(f"Weather in {city}:")
            icon_url = f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
            st.image(icon_url, width=100)
            
            # Display weather data in columns for better readability
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Temperature:** {weather_data['temp']}°C")
                st.markdown(f"**Pressure:** {weather_data['pressure']} hPa")
            with col2:
                st.markdown(f"**Humidity:** {weather_data['humidity']}%")
                st.markdown(f"**Wind Speed:** {weather_data['wind_speed']} m/s")
            
            # Sunrise and Sunset times
            st.markdown(f"**Sunrise:** {weather_data['sunrise']}")
            st.markdown(f"**Sunset:** {weather_data['sunset']}")
        else:
            st.error("Could not fetch weather data for the given city. Please try again.")

    else:
        st.warning("Please enter a city name to get the weather information.")
    
    st.markdown("""
        <hr>
        <p style="text-align: center; font-size: 16px;">Made by Pranishraj Atul Nigade</p>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
