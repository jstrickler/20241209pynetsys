city = 'Orlando'
temp = 85
count = 5
avg = 3.4563892382
flag = True

print(f"{city = }")    # default is raw view
print(f"{city = !s}")  # forces normal str view
print(f"{temp = }")
print(f"{count = }")
print(f"{count = :05d}")  # add formatting
print(f"{avg = :.2f}")    # add formatting
print(f"{flag = }")
