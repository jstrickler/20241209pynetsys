cities = []  # empty list
cities = list() # empty list
cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)  # don't use cities.append(more_cities)
print(f"cities: {cities}\n")

# LIST.append(obj) LIST.insert(idx, obj) LIST.extend(iterable)

del cities[3] 
print(f"cities: {cities}\n")

cities.remove('Buffalo')  # remove 1st occurrence of 'Buffalo' or error
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

# del LIST[idx]  LIST.remove(value) LIST.pop() LIST.pop(idx)    