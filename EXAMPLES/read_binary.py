# print out a file 10 bytes at a time

with open("../DATA/parrot.txt", "rb") as parrot_in: # Add "b" to "r", "w", or "a" for binary mode
    while True:
        chunk = parrot_in.read(10)  # Use read() to read a specified number of bytes
        if chunk == b"":   # Read returns bytes, not str
            break
        print(chunk.decode()) # Use decode() to convert bytes to str
