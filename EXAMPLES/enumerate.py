colors = "red blue green yellow brown black".split()

months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

colors_enum = enumerate(colors)
print(f"{colors_enum = }")
print(f"{list(colors_enum) = }\n")  # consumes enumerate values

colors_enum = enumerate(colors)

# enumerate() returns iterable of (index, value) tuples
for i, color in colors_enum:  
    print(i, color)
print()

# Second parameter to enumerate is added to index
for num, month in enumerate(months, 1):
    print(f"{num} {month}")
