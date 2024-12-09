file_path = "Projects/alpha/src/utils/pdfstuff.py"

print("file_path =", file_path)
print("len(file_path) =", len(file_path))

print("file_path.upper() =", file_path.upper())
print("file_path.count('/') =", file_path.count('/'))
print("file_path.count('p') =", file_path.count('p'))
print("file_path.lower().count('p') =", file_path.lower().count('p'))
print("file_path.startswith('Projects') =", file_path.startswith('Projects'))
print("file_path.endswith('.py') =", file_path.endswith('.py'))
print("file_path.removesuffix('.py') =", file_path.removesuffix('.py'))
print("'alpha' in file_path =", 'alpha' in file_path)
print("'beta' in file_path =", 'beta' in file_path)
print("file_path.find('alpha') =", file_path.find('alpha')) # also s.index()
print("file_path.find('beta') =", file_path.find('beta'))
print("file_path.replace('alpha', 'beta') =", file_path.replace('alpha', 'beta'))
print("file_path.split('/') =", file_path.split('/'))
parts =file_path.split('/')
print("parts =", parts)
print("':'.join(parts) =", ':'.join(parts))
print()

title = "   Why I love Python    "
print("title = [" + title + "]")
print("title.strip() = [" +  title.strip() + "]")
print("title.lstrip() = [" + title.lstrip() + "]")
print("title.rstrip() = [" + title.rstrip() + "]")












