city = 'Orlando'
temperature = 85
hit_count = 5
average = 3.4563892382

# variables inserted into string
print("It is %d\u00B0 in %s" % (temperature, city))
print()

# :03d means format (decimal) integer in 3 characters, 
#      left-padded with zeros
# :.2f means round a float to 2 decimal points
print(f"hit count is %03d average is %.2f" % (hit_count, average))
print()

# any expression is OK
print(f"2 + 2 is %d" % (2 + 2))

