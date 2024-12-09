import sys

for file_name in sys.argv[1:]:
    with open(file_name) as file_in:
        for i, line in enumerate(file_in, 1):
            print(f"{i:4d}: {line.rstrip()}")


