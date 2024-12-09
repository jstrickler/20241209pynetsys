from temp_conv import f2c

temp_str = input("Enter Fahrenheit temp: ")
fahrenheit = float(temp_str)
celsius = f2c(fahrenheit)

print(f"{fahrenheit:.1f} F is {celsius:.1f} C")

