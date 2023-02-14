"""
Write a function called forecast that stores information about the weather, and returns sorted information for all locations.
The function will receive a different number of arguments. The arguments will be passed as tuples with two elements -
the first one is the location, and the second one is the weather:
•	Location name: string
o	any string
•	Weather: string
o	"Sunny"
o	"Rainy"
o	"Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations
with cloudy weather, and last are the locations with rainy weather. For each sequence of locations (e.g. all sunny locations),
sort them by their name in ascending order (alphabetically).
In the end, return the output as described below.
"""


def forecast(*args):
    weather_data = {}
    for city, weather in args:
        weather_data[city] = weather

    sunny_location = sorted([loc for loc, condition in weather_data.items() if condition == 'Sunny'])
    cloudy_location = sorted([loc for loc, condition in weather_data.items() if condition == 'Cloudy'])
    rainy_location = sorted([loc for loc, condition in weather_data.items() if condition == 'Rainy'])

    sorted_location = sunny_location + cloudy_location + rainy_location

    output = []

    for location in sorted_location:
        output.append(f"{location} - {weather_data[location]}")

    return "\n".join(output)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
