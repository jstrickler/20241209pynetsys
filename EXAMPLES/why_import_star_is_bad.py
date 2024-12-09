from electrical import current, voltage, amps  # import current _explicitly_ from electrical
from navigation import *  # import current _implicitly_ from navigation

print(current())  # calls navigation.current(), not electrical.current()
print(voltage())
print(amps())
