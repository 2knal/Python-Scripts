#! /usr/bin/python3

# Random Password Generator

import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
password = ''
t = int(input("Length of password: "))
for i in range(t):
	password += random.choice(chars)
print(password)