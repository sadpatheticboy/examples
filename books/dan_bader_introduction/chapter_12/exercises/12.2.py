import pathlib

print(pathlib.Path.cwd())

# path = pathlib.Path.home()
path = pathlib.Path.home() / 'hello.txt'
print(path.exists())

# exercises
file_path = pathlib.Path.home() / 'my_file.txt'
exist = file_path.exists()
print(file_path.stem)
print(list[file_path.parents][-2])
