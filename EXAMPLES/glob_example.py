from glob import glob

files = glob('../DATA/*.csv') # expand file name wildcard into sorted list of matching names
print(files, '\n')

no_files = glob('../DATA/*.avi')
print(no_files, '\n')

