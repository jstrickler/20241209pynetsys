
import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

pattern = r'([A-Z])-(\d{2,3})'  # parens delimit groups

print("Group 0            Group 1              Group 2")
header2 = "text  start  end   text  start  end     text  start  end"
print(header2)
print("-" * len(header2))

for m in re.finditer(pattern, s):
    print(
        f"{m.group(0):5s}  {m.start(0):3d}  {m.end(0):3d}"
        f"    {m.group(1):5s}  {m.start(1):3d}  {m.end(1):3d}"
        f"      {m.group(2):5s}  {m.start(2):3d}  {m.end(2):3d}"
    )
print()

matches = re.findall(pattern, s)  # findall() returns list of tuples containing groups
print("matches:", matches)
