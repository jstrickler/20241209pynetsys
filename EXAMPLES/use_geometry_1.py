import sys
import geometry # find geometry.py

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module/path search order
# 1. current folder
# 2. folders in PYTHONPATH (if it exists)  (matches PATH variable)
# 3. sys.prefix/lib/***

print(f"{sys.prefix = }")
print()

for path in sys.path:
    print(path)

