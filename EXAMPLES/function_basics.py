# define function
def say_hello():
    print("Hello, world")

say_hello()  # Call function

def process_file(*file_paths):
    pass  # open file_path and use it

process_file("spam.txt", "ham.txt", "eggs.txt")
process_file()


def faux_grep(search_term, *file_paths, linenumbers=False):
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line_number, raw_line in enumerate(file_in, 1):
                if search_term in raw_line:
                    if linenumbers:
                        print(f"{line_number:4d}",  end=" ")
                    print(raw_line.rstrip())

faux_grep("bird", "../DATA/alice.txt", "../DATA/parrot.txt", linenumbers=True)




