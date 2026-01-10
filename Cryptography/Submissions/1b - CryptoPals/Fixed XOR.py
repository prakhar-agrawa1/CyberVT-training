from pwn import *

def myXOR(buff1, buff2):
    new_b1 = bytes.fromhex(buff1)
    new_b2 = bytes.fromhex(buff2)
    return bytes.hex(xor(new_b1, new_b2))

buff1 = "1c0111001f010100061a024b53535009181c"
buff2 = "686974207468652062756c6c277320657965"
end = "746865206b696420646f6e277420706c6179"

# print(xor(buff1,buff2))
print(myXOR(buff1, buff2))