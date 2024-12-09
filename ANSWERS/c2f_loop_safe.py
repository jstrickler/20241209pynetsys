while True:
    celsius = input('Enter Celsius temp: ')
    if celsius.lower().startswith('q'):
        break
    try:
        celsius = float(celsius)
    except ValueError as err:
        print(err)
        continue
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f"{celsius:.1f} C is {fahrenheit:.1f} F")

