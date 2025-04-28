

temperatures_fahrenheit = [32, 50, 77, 100, 212]

celsius_temps = [(temp - 32) * 5/9 for temp in temperatures_fahrenheit]

print(f"Temperature in Fahrenheit is: {temperatures_fahrenheit}")
print(f"Temperature in Celsius is:{celsius_temps}")