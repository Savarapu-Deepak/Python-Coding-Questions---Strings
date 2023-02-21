# Python Program to remove given character from string.

data = input('Enter Any String : ')
element = input('Enter Character to be removed : ')
res = data.replace(element, '')  # replace(old, new, count)
print(res)
