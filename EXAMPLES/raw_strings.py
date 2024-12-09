regex = r"the\b\b\bend"
file_path = r"c:\temp"
message = r"please put a newline character (\n) after each line"

print("** raw strings **")
print(regex)
print(file_path)
print(message)
print()

regex = "the\b\b\bend"
file_path = "c:\temp"
message ="please put a newline character (\n) after each line"

print("** non-raw **")
print(regex)
print(file_path)
print(message)
