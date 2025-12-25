1import requests
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch historical weather data
def fetch_weather_data(api_key, location, start_date, end_date):
    url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={start_date}&end_dt={end_date}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to calculate probability of a specific weather pattern
def calculate_probability(data, pattern):
    total_days = len(data['forecast']['forecastday'])
    pattern_days = sum(1 for day in data['forecast']['forecastday'] if pattern in day['day']['condition']['text'].lower())
    probability = (pattern_days / total_days) * 100
    return probability

# Function to plot the results
def plot_probability(probability, pattern):
    labels = ['Pattern Days', 'Other Days']
    sizes = [probability, 100 - probability]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)  # explode 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f'Probability of {pattern.capitalize()}')
    plt.show()

# Main function of the Probability Model
def main():
    api_key = ""  # Replace with your API key
    location = input("Enter the location: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    pattern = input("Enter the weather pattern to check (e.g., rain): ").lower()

    data = fetch_weather_data(api_key, location, start_date, end_date)
   , pattern)
    print(f"The probability of {pattern} in {location} from {start_date} to {end_date} is {probability:.2f}%")
    plot_probability(probability, pattern)

if __name__ == "__main__":
    main()


















