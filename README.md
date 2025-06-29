# API-INTEGRATION-AND-DATA-VISUALIZATION

Learning API Integration and Data Visualization

![Image](https://github.com/user-attachments/assets/417f1b00-134c-42cd-ba97-3e6ad9bd8d2e)

![Image](https://github.com/user-attachments/assets/3bebd73e-03e2-4051-86e0-9dd5b5eed63a)

COMPANY : CODTECH IT SOLUTIONS

NAME : Souvik Shomenath Dutta

INTERN I'D : CT06DH660

DOMAIN : Python Programming

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

DESCRIPTION : 

Project Title: API-INTEGRATION AND DATA-VISUALIZATION USING OPEN WEATHER MAP API

Project Overview

My project demonstrates how to integrate the OpenWeatherMap API with Python to fetch, process, and visualize weather forecast data for a given city. The project demonstrates on how to securely access the api, parse the returned data, and present it in a user-friendly graphical format using Python’s MatPlot Lib Module.

Features

API Integration:
The project uses the OpenWeatherMap 5-day/3-hour forecast API to retrieve weather data for a specified city. The API key is securely managed using environment variables and the python-dotenv library, preventing accidental exposure of sensitive credentials in the source code.

Data Retrieval and Parsing:
Upon making a successful API request, the project parses the JSON response to extract relevant weather information, such as temperature, weather description, and humidity for the first forecasted time slot. It also processes the entire forecast list to extract date-time and temperature pairs for visualization.

Error Handling:
The script checks the HTTP response status code to ensure the API call was successful. If the request fails (e.g., due to an invalid API key or network issue), a clear error message is displayed, and the script avoids attempting to process invalid data.

Data Visualization:
Using the matplotlib library, the project plots a line graph of temperature forecasts over time. The graph includes labeled axes, a descriptive title, and formatted date-time values, making it easy for users to interpret the forecast trends for the selected city.

Modular and Secure Code:
The code is organized for clarity and maintainability. Sensitive information like the API key is loaded from a .env file, following best practices for security. The script is easily adaptable to other cities by changing a single variable.

How It Works

Setup:
The script begins by importing necessary libraries: requests for HTTP requests, matplotlib.pyplot for plotting, datetime for date-time parsing, dotenv for environment variable management, and os for accessing environment variables.

API Key Management:
The API key is stored in a .env file and loaded into the script using load_dotenv(). This approach keeps the key out of the source code and version control.

API Request:
The script constructs the API endpoint URL using the specified city and API key, then sends a GET request to OpenWeatherMap.

Response Handling:
If the response status code is 200 (OK), the script parses the JSON data to extract and print the current forecast’s temperature, weather description, and humidity. It then processes the full forecast list to extract date-time and temperature values for plotting.

Visualization:
The extracted data is plotted as a line graph, showing how the temperature is expected to change over the forecast period. The graph is displayed using matplotlib.

Error Reporting:
If the API request fails, the script prints an informative error message, including the HTTP status code.

Use Cases and Extensions

Educational Tool:
This project serves as a practical example for students learning about APIs, JSON data handling, and data visualization in Python.

Customizable Forecasts:
Users can easily modify the script to fetch forecasts for different cities or extend it to visualize other weather parameters, such as humidity or wind speed.

Integration with Other Applications:
The core logic can be integrated into larger applications, such as weather dashboards, mobile apps, or IoT devices.

Conclusion

This project provides a comprehensive introduction to API integration and how to visualize data with the help of Python.
