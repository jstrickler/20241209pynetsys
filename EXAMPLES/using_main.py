import sys

# main function -- program entry point
# "main" is not a reserved word, but a strong convention
def main(args):
    function1()
    function2()

# other functions (could be imported)
def function1():
    print("hello from function1()")

def function2():
    print("hello from function2()")

if __name__ == '__main__':
    # Call main() with the command line parameters 
    # (omitting the script itself)
    main(sys.argv[1:])  
