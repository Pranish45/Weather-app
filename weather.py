import streamlit as st
import requests

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
        
        return {
            'temp': temp,
            'pressure': pressure,
            'humidity': humidity,
            'weather_description': weather_description,
            'wind_speed': wind_speed
        }
    else:
        return None  # If the city is not found or API error occurs

# Streamlit UI
def main():
    st.title('Weather App')

    api_key = "a0b539b5b0a9bcec8e37933a569d13f6"  # Replace with your OpenWeatherMap API key
    city = st.text_input("Enter city name", "")

    if city:
        weather_data = get_weather(city, api_key)

        if weather_data:
            st.subheader(f"Weather in {city.capitalize()}:")
            st.write(f"Temperature: {weather_data['temp']}°C")
            st.write(f"Pressure: {weather_data['pressure']} hPa")
            st.write(f"Humidity: {weather_data['humidity']}%")
            st.write(f"Weather Description: {weather_data['weather_description'].capitalize()}")
            st.write(f"Wind Speed: {weather_data['wind_speed']} m/s")
        else:
            st.error("City not found or invalid API key!")

if __name__ == "__main__":
    main()
