# str = input("Please enter a string:")
# key = int(input("Please enter a key:"))
# encrypt_message = ""

# for i in str:
#     add = ord(i)+key
#     chat = chr(add)
#     encrypt_message += chat

# orignal_word = ""
# for x in encrypt_message:
#     asci = ord(x)-key
#     alphabet = chr(asci)
#     orignal_word += alphabet

# print(encrypt_message)
# print(orignal_word)
str =input("please enter a string")
key =int("please enter a key")
encrypt_message=""

for i in str:
    odd = odd(i)+key
    chat = chr(odd)
    encrypt_message +=chat


orignal_word =""
for x in encrypt_message:
    asci = odd(x)-key
    alphabet = chr(asci)
    orignal_word +=alphabet


print(encrypt_message)
print(orignal_word)

