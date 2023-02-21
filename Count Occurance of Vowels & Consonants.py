# Python Program to count vowels and consonants in a string.

data = input('Enter Any String : ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowels_Count = 0
consonants_Count = 0

for char in data:
    if char in vowels:
        vowels_Count += 1
    else:
        consonants_Count += 1
else:
    print('Vowels Count : ', vowels_Count)
    print('Consonants Count : ', consonants_Count )