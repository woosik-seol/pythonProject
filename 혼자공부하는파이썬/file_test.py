
with open("noname.txt", 'w') as file:
    file.write("HelloWorld!1\n")
    file.write("HelloWorld!2")

with open("noname.txt", 'r') as file:
    contents = file.read()

print(contents)
# HelloWorld!1
# HelloWorld!2


with open("noname.txt", 'r') as file:
    contents1 = file.readline()
    contents2 = file.readline()

print(contents1 + contents2)
# HelloWorld!1
# HelloWorld!2



