#
import shlex

cmd = 'herp derp "fuzzy bear" "wanga tanga" pop'  # Command line with quoted whitespace

print(cmd.split())  # Normal split does the wrong thing
print()

print(shlex.split(cmd))  # shlex.split() does the right thing
