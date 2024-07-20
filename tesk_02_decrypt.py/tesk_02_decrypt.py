alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

key = []
import random
while len (key) < 26:
    ran = random.choice(alphabet)
    key.append(ran)
    if key. count(ran)> 1:
        key.remove(ran)
        print(alphabet)
        print(key)


string = input("please enter a string")
encrypt_message =""

for str in string:
    if str in alphabet:
        index =alphabet.index(str)
        if str in key:
            word_in_key =key[index]
            encrypt_message +=str
else:
    encrypt_message +=str

    decrypt_message =""
    for char in encrypt_message:
        if char in key:
            ind = key.index(char)
            if char in alphabet:
                word_in_alphabet= alphabet[ind]
                decrypt_message += word_in_alphabet
print(encrypt_message)
print(decrypt_message)



