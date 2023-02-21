# Python Program to check given character is vowel or consonant

data = input('Enter Any CHaracter from a to z : ')
check = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if data in check:
    print(data, 'is a Vowel')
else:
    print(data, 'is not a vowel')