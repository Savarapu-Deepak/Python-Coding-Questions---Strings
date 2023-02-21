# Python Program to print highest frequency of a given character.

data = input('Enter Any Data : ')
check = input('Enter any Character : ')
count = 0

for char in data:
    if char == check:
        count += 1
else:
    print('Count of Character : ', count)