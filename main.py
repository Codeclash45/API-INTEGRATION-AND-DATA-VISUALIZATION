#Import Libraries
import requests
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv("API_KEY") #Declaring API KEY (To prevent hardcoding, I have used .env file to store the API KEY)
CITY = 'Mumbai' #Declaring the CITY
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric' # The URL to which requests would be sent

# Send request
response = requests.get(URL)

#Using an if loop which displays the forecast data upon receiving 200 status code which means the api is working
if response.status_code == 200:
    data = response.json()
    first_forecast = data["list"][0]
    print("Weather of ", CITY)
    print("The Temperature is as follows : ", first_forecast["main"]["temp"], "°C")
    print("The Weather is as follows : ", first_forecast["weather"][0]["description"].capitalize())
    print("The Humidity is as follows : ", first_forecast["main"]["humidity"], "%")
else:
    print("The Data could not be retrieved because an error occured. The error code is : ", response.status_code)
    
#Parsing the dates and temperatures
dates = [datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S") for item in data['list']]
temps = [item['main']['temp'] for item in data['list']]

#Plotting the graph using matplotlib - python module
plt.figure(figsize=(10, 5)) #Setting the figure size for the plot (You can customize it)
plt.plot(dates, temps, marker='o', linestyle='-', color='b') #Defining the styles
plt.title(f"Temperature Forecast for {CITY}") #The title of the graph
plt.xlabel("Date and Time") #Label for X-Axis
plt.ylabel("Temperature (°C)") #Label for Y-Axis
plt.tight_layout() #Properly display the graph
plt.show() #Showing the graph