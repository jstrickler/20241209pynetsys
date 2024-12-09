city = 'Orlando'
temperature = 85
hit_count = 5
average = 3.4563892382

# variables inserted into string
print("It is {}\u00B0 in {}".format(temperature, city))
print()

# :03d means format (decimal) integer in 3 characters, 
#      left-padded with zeros
# :.2f means round a float to 2 decimal points
print("hit count is {:03d} average is {:.2f}".format(hit_count, average))
print()

# any expression is OK
print("2 + 2 is {}".format(2 + 2))

