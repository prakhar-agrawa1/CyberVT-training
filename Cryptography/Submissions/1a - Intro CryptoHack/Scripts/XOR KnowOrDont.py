from pwn import *

enc = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"); print(enc)

for i in range(len(enc)):
    curr = enc[0:i]
    key = xor(curr, "crypto{")
    print(key)

# Key = myXORkey? Recurring string in output.

flag = xor(enc, "myXORkey")
print(flag)