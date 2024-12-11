from subprocess import run, PIPE, SubprocessError, CalledProcessError
import shlex

raw_command = "netstat -n"

command_words = shlex.split(raw_command)

# files = glob("folder/*.txt")
# command_words += files

print(f"{command_words = }")

process = run(command_words, stdout=PIPE)
# print(type(process.stdout.decode()))
# print(process.stdout.decode())

output_lines = process.stdout.decode().splitlines()

established_connections = [line for line in output_lines if "ESTABLISHED" in line]
# for line in output_lines:
#     if "ESTABLISHED" in line:
#         print(line)


