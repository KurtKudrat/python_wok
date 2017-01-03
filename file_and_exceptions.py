filename = 'python_text.txt'


# reading the entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)


#reading the file line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#store the file in a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:

    print(line.rstrip())


#working with a file's content
with open(filename) as file_object:
    lines = file_object.readlines()

read_line = ''
for line in lines:
    read_line += line.rstrip()


print(read_line)
