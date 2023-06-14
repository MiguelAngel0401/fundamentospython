my_string="estE eS un TexTo"
print(type(my_string))

print(my_string.capitalize())
print(my_string.upper())
print(my_string.lower())
print(my_string.title())

print(len(my_string))

#Indexing
my_string="Hola Alumnos"

print(my_string[3])
for letter in my_string:
    print(f"la letra {letter}")

print(my_string[-1])
print(my_string[-2])

#Slicing
print(my_string[:])
print(my_string[0:3])
print(my_string[3:])
print(my_string[3:7])
print(my_string[:7])
print(my_string[::-1])