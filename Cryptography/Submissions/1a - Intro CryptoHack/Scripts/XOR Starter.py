from pwn import *

def myXor(input, key):
    output = ""
    for char in input:
        new_char = xor(char, key)
        print(char, "XOR", str(key), "=", new_char)
        output += str(new_char)
    return output


#

word = "label"
key_per_char = 13

print(myXor(word, key_per_char))

print(xor(word, key_per_char))

# Got 'aloha'