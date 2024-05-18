import re

def is_palindrome(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

user_input = input("Введите строку: ")
if is_palindrome(user_input):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
