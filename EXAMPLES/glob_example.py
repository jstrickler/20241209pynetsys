from glob import glob

files = glob('../DATA/*.txt') # expand file name wildcard into sorted list of matching names
print(files, '\n')

no_files = glob('../JUNK/*.avi')
print(no_files, '\n')

