import sys


# other imports  (standard library, standard non-library, local)

# constants (AKA global variables)

# main function
def main(args):  # Program entry point. While main is not a reserved word, it is a strong convention
    function1()
    function2()


# other functions
def function1():
    print("hello from function1()")


def function2():
    print("hello from function2()")


if __name__ == '__main__':
    main(sys.argv[1:])  # Call main() with the command line parameters (omitting the script itself)
