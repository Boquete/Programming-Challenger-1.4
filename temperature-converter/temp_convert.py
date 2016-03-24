temperature = int(input("What's the temperature to convert: "))
unit = input("What unit is it? (fahrenheit, celsius or kelvin)")


def user_input(unit):
    if unit == "fahrenheit":
        fahrenheit(temperature)
    elif unit == "celsius":
        celsius(temperature)
    elif unit == "kelvin":
        kelvin(temperature)
    else:
        print("You misspelled something.")


def celsius(temp):
    print(temp, "°C is: ")
    print("*", temp * 9 / 5 + 32, "°F")
    print("*", temp + 273.15, "K")


def fahrenheit(temp):
    print(temp, "°F is: ")
    print("*", (temp - 32) / 1.8, "°C")
    print("*", (temp + 459.67) * 5 / 9, "K")


def kelvin(temp):
    print(temp, "K is: ")
    print("*", temp - 273.15, "°C")
    print("*", temp * 9 / 5 - 459.67, "°F")


user_input(unit)
