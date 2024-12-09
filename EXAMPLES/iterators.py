colors = ['red', 'green', 'purple']

colors_rev = reversed(colors)
print(f"{colors_rev = }")
for color in colors_rev:
    print(color)
print()

first_names = "Bill Bill Dennis Steve Larry".split()
last_names = "Gates Joy Richie Jobs Ellison".split()

full_names = zip(first_names, last_names)  # zip() returns an iterator of tuples created from corresponding elements
print("full_names:", full_names)
print()

for first_name, last_name in full_names:
    print(f"{first_name} {last_name}")
