import sys
from knight import Knight

for name in sys.argv[1:]:
    k = Knight(name)
    print(f"Name: {k.title} {name}")
    print("Favorite Color:", k.favorite_color)
    print()
