import urllib.request

response = urllib.request.urlopen("https://www.python.org")

print(response.info())  # .info() returns a dictionary of HTTP headers
print()

print(response.read(500).decode())   # The text is returned as a bytes object, so it needs to be decoded to a string
