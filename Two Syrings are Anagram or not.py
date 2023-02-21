# Python Program to Check two strings are anagram or not.

data_1 = input('Enter  String_1 : ')
data_2 = input('Enter String_2 : ')

if len(data_1) != len(data_2):
    print('Strings are not Anagram')
else:
    if sorted(data_1) == sorted(data_2):
        print('Strings are Anagram')


