def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


while True:
    conversion = input(
        "\nDo you wish to convert Celsius to Fahrenheit (C), or Fahrenheit to Celsius (F)?  (Type 'Q' to quit)\n:").lower()
    if conversion == "q":
        print("Thanks for trying me out. :-)")
        quit()
    elif conversion == "c":
        celsius = input("\nWhat temperature would you like to convert?\n:")
        if not celsius.isdigit():
            print("That's an invalid entry.")
            continue
        else:
            print(f"{int(celsius)}°C is equal to {
                  celsius_to_fahrenheit(int(celsius)):.2f}°F")
    elif conversion == "f":
        fahrenheit = input("What temperature would you like to convert?\n:")
        if not fahrenheit.isdigit():
            print("That's an invalid entry.")
            continue
        print(f"{int(fahrenheit)}°F is equal to {
              fahrenheit_to_celsius(int(fahrenheit)):.2f}°C")
    else:
        print("That's not a valid entry.")
        continue