FILE_PATH = "../DATA/ctemps.txt"

def c2f(celsius):
    fahrenheit = ((9 * celsius) / 5) + 32
    return fahrenheit

with open(FILE_PATH) as ctemps_in:
    for raw_line in ctemps_in:
        c_temp = float(raw_line)
        f_temp = c2f(c_temp)
        print(f"{c_temp} C is {f_temp} F")