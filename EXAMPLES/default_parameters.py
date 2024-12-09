def spam(greeting, whom='world'):  # 'world' is default value for positional parameter whom
    print(f"{greeting}, {whom}")


spam("Hello", "Mom")  # parameter supplied; default not used
spam("Hello")  # parameter not supplied; default is used
print()

def ham(*, file_name, file_format='txt'):  # 'world' is default value for named parameter format
    print(f"Processing {file_name} as {file_format}")

ham(file_name='eggs')  # parameter format not supplied; default is used
ham(file_name='toast', file_format='csv')
