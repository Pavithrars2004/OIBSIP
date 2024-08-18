import requests

def get_weather(api_key, city):
    # Base URL for OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send a request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant information
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        
        # Print weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found. Please check the city name.")

def main():
    api_key = "0cc6f7848b096817c8ab4b221a26bc00"
    city = input("Enter the city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()
