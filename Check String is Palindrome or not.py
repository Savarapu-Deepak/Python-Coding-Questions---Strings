# Python Program to check string is Palindrome or not.
data = input('Enter Any String : ')
rev = ''
for item in data:
    rev = item + rev
else:
    if rev == data:
        print(rev, 'is Anagram')
    else:
        print(rev, 'not an Anagaram')