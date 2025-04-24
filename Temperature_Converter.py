print("Temperature Converter")
temp = float(input("Enter the temperature: "))
print("Chose the conversion:")
options = ["1.Celsius to Fahrenheit",
           "2.Fahrenheit to Celsius",
           "3.Celsius to Kelvin",
           "4.Kalvin to Celsius"]

for option in options:
    print(option)

choice = input("Enter your choice (1-4): ")

if choice == "1":
    fahrenheit = (temp * 1.8) + 32
    print(f"{fahrenheit}°F")

elif choice == "2":
    celsius = (temp - 32) / 1.8
    print(f"{celsius}°C")

elif choice == "3":
    celsius = (temp + 273.15)
    print(f"{temp} = {celsius} K")

elif choice == "4":
    kalvin = (temp - 273.15)
    print(f"{kalvin} = {temp}°C")




