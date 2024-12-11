import sys
import fileinput
from argparse import ArgumentParser
import re

#  fauxgrep.py -i -f search-term file1 file2 file3 ...

parser = ArgumentParser(description="""
fauxgrep -- search files for patterns
                        
Usage:
python fauxgrep.py PATTERN FILE FILE ....
""")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-f", dest="print_name", action="store_true", help="Print file name")
parser.add_argument("-n", action="store_true", dest="line_numbers", help="Show line number")
parser.add_argument("search_term", help="Search term to find")
parser.add_argument("files", nargs="*", help="Files to search")

args = parser.parse_args()  

search_term_re = re.compile(args.search_term, re.I if args.ignore_case else 0)

for raw_line in fileinput.input(args.files):
    if search_term_re.search(raw_line):
        line = raw_line.rstrip()
        if args.print_name:
            print(fileinput.filename(), end=" ")
        if args.line_numbers:
            print(f"{fileinput.filelineno()}:", end=" ")
        print(line)
