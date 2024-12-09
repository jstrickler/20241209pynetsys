import sys
import re

if len(sys.argv) < 3:
    print("Usage: pfind PATTERN file ...")
    sys.exit(1)

try:
    pattern = re.compile(sys.argv[1])
except re.error as err:
    print(f"Error compiling RE: {err}")
    sys.exit()

for file_name in sys.argv[2:]:
    try:
        file_in = open(file_name)
    except IOError as err:
        print(f"Unable to open {file_name}: {err}")
        continue
    else:
        for line in file_in:
            if pattern.search(line):
                print(f"{file_name}: {line}", end=' ')
        file_in.close()
