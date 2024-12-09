"""
Script to read knight data from a file and display it.
"""
from pprint import pprint

FILE_PATH = "../DATA/knights.txt"

def main():  # named 'main' by *convention*
    """
    Program entry point
    """
    info = read_knight_data(FILE_PATH)
    pretty_print_knight_data(info)
    print()
    print_titles(info)
    print()
    robin_color = get_field_value(info, 'Robin', 1)
    print(f"{robin_color = }")
    
def read_knight_data(file_path):
    """
    Read the knight data from a file and put it in a dictionary.

    The dictionary key is a string containing the knight's name.

    The value is a tuple with the title, favorite color, quest, and comment for 
    the knight.
    """
    data = {}

    with open(file_path) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(":")

            # key is knight's name
            # value is tuple of fields
            data[name] =  title, color, quest, comment  

    return data

def pretty_print_knight_data(knight_info):
    """
    Pretty-print the knight data structure
    """
    pprint(knight_info)

def print_titles(knight_info):
    """
    Print all of the knights with their titles
    """
    for name, info in knight_info.items():
        print(f"{info[0]} {name}")

def get_field_value(knight_info, knight, field_index):
    """
    Return one field from a specified knight
    """
    return knight_info[knight][field_index]

if __name__ == "__main__":
    main()