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

# Function to fetch background image from Unsplash API
def get_background_image(city, unsplash_api_key):
    url = f"https://api.unsplash.com/photos/random?query={city}&client_id={unsplash_api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            image_url = data[0]['urls']['regular']  # Get the regular-sized image
            return image_url
    return None  # If no image found, return None

# Function to load a default image if no background image found
def load_default_image(city):
    default_images = {
        "Pune": "https://example.com/pune_default_image.jpg",  # Replace with an actual image URL or path
        "London": "https://example.com/london_default_image.jpg",  # Example for London
        "New York": "https://example.com/ny_default_image.jpg",  # Example for New York
    }
    # Check if the city has a default image, otherwise use a generic default background
    return default_images.get(city, "https://example.com/default_background_image.jpg")  # A generic default

# Streamlit UI
def main():
    # Set the page title and theme
    st.set_page_config(page_title="Weather App", page_icon=":sunny:", layout="centered")
    st.title("🌦️ Weather App 🌦️")
    
    # API Keys (ensure you replace with your own keys)
    weather_api_key = "a0b539b5b0a9bcec8e37933a569d13f6"  # Replace with your OpenWeatherMap API key
    unsplash_api_key = "YRux8h5eNPiVRTMfGZpKnq6sJBSntri5RAVpH87ZLQ0"  # Replace with your Unsplash API key
    
    # Add some spacing for aesthetics
    st.markdown("<br>", unsafe_allow_html=True)
    
    # User input for city name
    city = st.text_input("Enter city name", "").capitalize()

    # Fetch the background image based on city name
    if city:
        background_image_url = get_background_image(city, unsplash_api_key)
        
        # If no background image is found, use default image
        if background_image_url:
            st.image(background_image_url, use_column_width=True)
        else:
            default_image_url = load_default_image(city)
            st.image(default_image_url, use_column_width=True)
            st.warning(f"No background image found for {city}, using default background.")
        
        # Make the app more interactive by displaying a button
        if st.button("Get Weather"):
            # Get the weather data
            weather_data = get_weather(city, weather_api_key)

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
                
            else:
                st.error("City not found or invalid API key!")
        else:
            st.warning("Please enter a city name to get weather data.")
    
    # Add footer with your name or any additional details
    st.markdown("""
        <hr>
        <p style="text-align: center; font-size: 16px;">Made by Pranish</p>
        """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
