# Python Program to replace space in a string with given charater

data = input('Enter Any String wiht Space : ')
element = input('Enter Character to be added : ')
res = ''
for i in data:
    if i == '':
        i = element
    res = res + i
print(res)

