import logging
# logging.basicConfig(
#     level=logging.DEBUG,
# )

numpairs = [(5, 1), (1, 5), (5, 0), (0, 5)]

total = 0

for x, y in numpairs:
    print(x, y)
    try:
        quotient = x / y
    except ZeroDivisionError as err:
        logging.warning(err)
    else:
        total += quotient  # Only if no exceptions were raised
    finally:
        print("OK")

print(total)

#  try except ... else finally



