message = "72\u00B0C"
print(f"message: {message}")
print(f"type(message): {type(message)}")
print(f"len(message): {len(message)}")
for i, char in enumerate(message):
    print(i, char)
print()

binary_message = message.encode()  # encode text to binary (using utf-8 encoding)
print(f"binary_message: {binary_message}")
print(f"type(binary_message): {type(binary_message)}")
print(f"len(binary_message): {len(binary_message)}")
for i, byte in enumerate(binary_message):
    print(i, byte)
print()

original_message = binary_message.decode()
print(f"original_message: {original_message}")
