from temp_conv import c2f

temp_str = input("Enter Celsius temp: ")
celsius = float(temp_str)
fahrenheit = c2f(celsius)

print(f"{celsius:.1f} C is {fahrenheit:.1f} F")

