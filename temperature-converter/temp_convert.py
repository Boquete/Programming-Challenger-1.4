temperature = int(input("What's the temperature to convert: "))
unit = input("What unit is it? (fahrenheit, celsius or kelvin)")


def fahrenheit_to_celsius(temp):
    return (temp - 32) / 1.8


def fahrenheit_to_kelvin(temp):
    return (temp + 459.67) * 5 / 9


def celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32


def celsius_to_kelvin(temp):
    return temp + 273.15


def kelvin_to_celsius(temp):
    return temp - 273.15


def kelvin_to_fahrenheit(temp):
    return temp * 9 / 5 - 459.67


if unit == "fahrenheit":
    print(temperature, "°F is: ")
    print("*", fahrenheit_to_celsius(temperature), "°C")
    print("*", fahrenheit_to_kelvin(temperature), "K")
elif unit == "celsius":
    print(temperature, "°C is: ")
    print("*", celsius_to_fahrenheit(temperature), "°F")
    print("*", celsius_to_kelvin(temperature), "K")
elif unit == "kelvin":
    print(temperature, "K is: ")
    print("*", kelvin_to_celsius(temperature), "°C")
    print("*", kelvin_to_fahrenheit(temperature), "°F")
else:
    print("You misspelled something.")
