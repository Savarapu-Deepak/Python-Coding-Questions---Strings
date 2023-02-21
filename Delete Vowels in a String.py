# Python Program to remove vowels in a given string.

data = input('Enter Any String  : ')
update = ''
check = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in data:
    if char in check:
        pass
    else:
        update = update + char
else:
    print(update)