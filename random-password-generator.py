from random import choice
len_of_password = 10
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
password = "".join(choice(password_chars) for x in range(len_of_password))
print(password)