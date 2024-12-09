import sys
from subprocess import check_output, Popen, CalledProcessError, STDOUT, PIPE # need to import PIPE and STDOUT
from glob import glob
import shlex

if sys.platform == 'win32':
    CMD = 'cmd /c dir'
    FILES = r'..\DATA\t*'
else:
    CMD = 'ls -ld'
    FILES = '../DATA/t*'

cmd_words = shlex.split(CMD)
cmd_files = glob(FILES)

full_cmd = cmd_words + cmd_files

# capture only stdout
try:
    output = check_output(full_cmd) # check_output() returns stdout
    print("Output:", output.decode(), sep='\n') # stdout is returned as bytes (decode to str)
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)

# capture stdout and stderr together
try:
    cmd = cmd_words + cmd_files + ['spam.txt']
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT) # assign PIPE to stdout, so it is captured; assign STDOUT to stderr, so both are captured together
    stdout, stderr = proc.communicate() # call communicate to get the input streams of the process; it returns two bytes objects representing stdout and stderr
    print("Output:", stdout.decode()) # decode the stdout object to a string
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)

try:
    cmd = cmd_words + cmd_files + ['spam.txt']
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE) # assign PIPE to stdout and PIPE to stderr, so both are captured individually
    stdout, stderr = proc.communicate() # now stdout and stderr each have data
    print("Output:", stdout.decode()) # decode from bytes and output
    print("Error:", stderr.decode()) # decode from bytes and output
except CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)
