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
        
        # Display weather info
        print(f"\nWeather in {city.capitalize()}:\n")
        print(f"Temperature: {temp}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or invalid API key!")

# Main function to ask the user for input and fetch weather data
def main():
    api_key = "a0b539b5b0a9bcec8e37933a569d13f6"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ").strip()
    
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
