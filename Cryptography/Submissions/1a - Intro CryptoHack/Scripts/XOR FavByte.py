from pwn import *

enc = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"); print(enc)
key = "unknown byte"
dec = "?"

i = 0

for i in range(128): # Searched online for this idea
    print(dec)
    if "crypto" in str(dec):
        break
    key = chr(i)
    dec = xor(enc, key)

print(key)