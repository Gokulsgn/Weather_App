import requests
import streamlit as st
from datetime import datetime  # Importing datetime module

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
    
    # Get current date and time in 12-hour format with AM/PM
    current_time = datetime.now().strftime("%Y-%m-%d / %I:%M:%S %p")

    # Use markdown with CSS for center alignment
    st.markdown(f"""
    <div style='text-align: center;'>
        <h2>Weather in {city}, {country}</h2>
        <p><strong>Date & Time:</strong> {current_time}</p>
        <p><strong>Temperature:</strong> {temp}°C</p>
        <p><strong>Condition:</strong> {weather_desc.capitalize()}</p>
        <p><strong>Humidity:</strong> {humidity}%</p>
        <p><strong>Wind Speed:</strong> {wind_speed} m/s</p>
    </div>
    """, unsafe_allow_html=True)

# Main function for the Streamlit app
def main():
    # Set the page configuration including the favicon
    st.set_page_config(
        page_title="Weather App",
        page_icon="https://cdn2.iconfinder.com/data/icons/weather-filled-outline-3/64/weather02-1024.png",  # Replace with your actual favicon URL
        layout="centered"
    )

    # Add CSS for centering the title
    st.markdown("""
    <style>
    .title-center {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Center the title
    st.markdown("<h1 class='title-center'>Weather App</h1>", unsafe_allow_html=True)

    # Insert your API key here
    api_key = "eeeb5bb7f4c6efab91db7759a94a7b31"  # Replace with your actual API key

    city = st.text_input("Enter city name:", "Chennai")  # Default city is Chennai

    if st.button("Get Weather"):
        data = get_weather_data(city, api_key)
        
        if data.get("cod") != 200:
            st.error(f"City {city} not found.")
        else:
            display_weather(data)

if __name__ == "__main__":
    main()
