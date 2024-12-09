a = 0b10101010  # a and b are integers
b = 0b11110000

c = a & b  # bitwise AND
print(f"  {a:08b}")
print(f"& {b:08b}")
print("  --------")
print(f"  {c:08b}")
print()

c = a | b # bitwise OR
print(f"  {a:08b}")
print(f"| {a:08b}")
print("  --------")
print(f"  {a:08b}")
print()

c = a ^ b # bitwise XOR
print(f"  {a:08b}")
print(f"^ {b:08b}")
print("  --------")
print(f"  {c:08b}")
print()

c = ~a # complement (flip bit values)
print(f" ~ {a:09b}")
print(f"   {a:09b}")
print()

c = a >> 1 # shift right 1 bit
print(f"{a:08b} >> 1")
print(f"{c:08b}")
print()

c = a >> 3 # shift right 3 bits
print(f"{a:08b} >> 3")
print(f"{c:08b}")
print()

c = a << 1 # shift left 1 bit
print(f"{a:012b} << 1")
print(f"{c:012b}")
print()

c = a << 3 # shift left 3 bits
print(f"{a:012b} << 3")
print(f"{c:012b}")
print()
