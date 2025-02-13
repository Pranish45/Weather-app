import requests

# Function to get weather data from OpenWeatherMap API
def get_weather(city, api_key):
    # OpenWeatherMap API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={a0b539b5b0a9bcec8e37933a569d13f6}&units=metric"  # For Celsius
    
    # Sending the request to the OpenWeatherMap API
    response = requests.get(complete_url)
    
    # If the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the response as JSON
        
        # Extracting data from the JSON response
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        # Extracting relevant details
        temp = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = weather['description']
        wind_speed = wind['speed']
        
        # Displaying the weather details
        print(f"\nWeather in {city.capitalize()}:\n")
        print(f"Temperature: {temp}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        # If the city is not found or there's an issue with the API call
        print("City not found or invalid API key!")

# Main function to get user input and display the weather data
def main():
    # Replace with your OpenWeatherMap API key
    api_key = "YOUR_API_KEY"  # Get your API key from https://openweathermap.org/api
    city = input("Enter city name: ").strip()  # User enters the city name
    
    # Call the function to get the weather for the entered city
    get_weather(city, api_key)

# Entry point of the script
if __name__ == "__main__":
    main()
