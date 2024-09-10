import requests
import streamlit as st

# Function to get weather data
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to display weather data
def display_weather(data):
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    st.write(f"**Weather in {city}, {country}:**")
    st.write(f"**Temperature:** {temp}°C")
    st.write(f"**Condition:** {weather_desc.capitalize()}")
    st.write(f"**Humidity:** {humidity}%")
    st.write(f"**Wind Speed:** {wind_speed} m/s")

# Function to get city suggestions
def get_city_suggestions(user_input, all_cities):
    suggestions = [city for city in all_cities if user_input.lower() in city.lower()]
    return suggestions

# List of cities for suggestions (you can replace this with a more extensive list or API)
all_cities = ["Chennai", "Mumbai", "Delhi", "Kolkata", "Bangalore", "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "New York", "London", "Paris", "Tokyo", "Sydney", "Toronto"]

# Main function for the Streamlit app
def main():
    st.set_page_config(page_title="Weather App", page_icon="☀️", layout="wide")

    st.title("Weather App")
    st.markdown("## Find out the current weather conditions for any city!")

    # Insert your API key here
    api_key = "eeeb5bb7f4c6efab91db7759a94a7b31"  # Replace with your actual API key

    # Input for city name
    city_input = st.text_input("Enter city name:", "Chennai")

    # Get suggestions based on user input
    if len(city_input) > 1:
        suggestions = get_city_suggestions(city_input, all_cities)
    else:
        suggestions = []

    # Provide a dropdown for suggestions
    city = st.selectbox("Select city:", options=suggestions, index=0) if suggestions else city_input

    # Button to fetch weather data
    if st.button("Get Weather"):
        with st.spinner("Fetching weather data..."):
            data = get_weather_data(city, api_key)
            if data.get("cod") != 200:
                st.error(f"City '{city}' not found. Please try again.")
            else:
                display_weather(data)

    # Add some footer information
    st.markdown("---")
    st.markdown("Made with ❤️ by [Gokul]")

if __name__ == "__main__":
    main()
