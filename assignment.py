str = input("Enter a string: ")

# a) Print the string as a list of individual characters
char_list = [char for char in str]
print("List of characters:", char_list)

# b) Find the length of the string (without using len)
length = 0
for _ in str:
    length += 1
print("Length of the string:", length)

# c) Find the minimum element after converting string to list
min_char = char_list[0]
for char in char_list:
    if char < min_char:
        min_char = char
print("Minimum element in the list:", min_char)

# d) Count number of spaces without using any built-in methods
space = 0
for char in str:
    if char == ' ':
        space += 1
print("Number of spaces:", space)
