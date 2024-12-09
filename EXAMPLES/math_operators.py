a = 23
b = 7

print(a + b, a - b, a * b)  # normal operations

print(a / b, a // b, a / -b, a // -b)   # division and floored division
  
print(a ** b)   # exponentiation

print(a % b)   # modulus (remainder)

x = 22
x += 10  # Same as x = x + 10
print(f"{x = }")
print()

print(f"{1 + 2 * 3 / 4 = }")
print(f"{(1 + 2) * (3 / 4) = }")
print(f"{(1 + (2 * 3)) / 4 = }")
print(f"{1 + ((2 * 3) / 4) = }")  # same as example without parens
