import re
import fileinput
import argparse

arg_parser = argparse.ArgumentParser(description="Emulate grep")  # argument parser

arg_parser.add_argument(
    '-i',
    dest='ignore_case', action='store_true',
    help='ignore case'
)  # add option to the parser; dest is name of option attribute

arg_parser.add_argument(
    '-n',
    dest='show_names', action='store_true',
    help='display file names'
)  # add option to the parser; dest is name of option attribute

arg_parser.add_argument(
    'pattern', help='Pattern to find (required)'
)  # add required argument to the parser

arg_parser.add_argument(
    'filenames', nargs='*',
    help='filename(s) (if no files specified, read STDIN)'
)  # add optional arguments to the parser

args = arg_parser.parse_args()  # actually parse the arguments

print('ARGS:', args, "\n")

regex = re.compile(args.pattern, re.I if args.ignore_case else 0)  # compile regex

for line in fileinput.input(args.filenames):  # loop over list of file names and read them one line at a time
    if regex.search(line):
        if args.show_names:
            print(fileinput.filename(), end=": ")
        print(line.rstrip())
