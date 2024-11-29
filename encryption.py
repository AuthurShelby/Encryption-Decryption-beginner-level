import random
import string

encryption = " "+string.punctuation+string.ascii_letters+string.digits
encryption = list(encryption)
encrypted = encryption.copy()
random.shuffle(encrypted)
encrypt = ""
userInput = input("enter a text to encrypt: ")
for i in userInput:
    index = encryption.index(i)
    encrypt += encrypted[index]
print(f"Original text: {userInput}")
print(f"Encrypted text-{encrypt}")
decryptInput=input("enter a decrypted text: ")
decrypt = ""
for i in decryptInput:
    if i in encrypted:
        index = encrypted.index(i)
        decrypt += encryption[index]
print(f"encryption: {encrypt}")
print(f"decrypted : {decrypt}")