city = 'Orlando' 
temperature = 85
hit_count = 5
average = 3.4563892382

print(city, temperature, hit_count, average)
print()

print(city, end=' ')  # Print space instead of newline at the end
print(temperature)
print()

# Item separator is comma + space
print(city, temperature, hit_count, average, sep=", ")
print()

# Item separator is empty string
print(city, temperature, hit_count, average, sep="")
print()
