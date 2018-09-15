#! /usr/bin/python3


# Encrypting through Caeser Cipher

alphabetLower = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
key = 3
newMessage = ""
message = input("Enter the character: ")


for character in message:
    if character in alphabetLower:
        position = alphabetLower.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabetLower[newPosition]
        newMessage += newCharacter
    elif character in alphabetUpper:
        position = alphabetUpper.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabetUpper[newPosition]
        newMessage += newCharacter
    elif character in numbers:
        position = numbers.find(character)
        newPosition = (position + key) % 26
        newCharacter = numbers[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

print(newMessage)
