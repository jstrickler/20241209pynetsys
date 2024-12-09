from struct import Struct

values = 7, 6, 42.3, b'Guido' # create some assoted values

demo = Struct('iif10s')  # create Struct object with desired data layout

print(f"Size of data: {demo.size} bytes") # size property gives size of data in bytes

binary_stream = demo.pack(*values) # pack() converts values into binary stream using format

int1, int2, float1, raw_bytes = demo.unpack(binary_stream) # unpack() converts binary stream into list of values
str1 = raw_bytes.decode().rstrip('\x00')  # decode the raw bytes into a string, and strip off trailing null bytes (that were added by pack())

print(f"raw_bytes: {raw_bytes}")
print(f"int1: {int1}")
print(f"int2: {int2}")
print(f"float1: {float1}")
print(f"str1: {str1}")

