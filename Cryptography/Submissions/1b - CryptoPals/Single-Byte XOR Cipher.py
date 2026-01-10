from pwn import *

hexa = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

end = bytes.fromhex(hexa)

key = "unknown character"

for i in range(128):
    key = chr(i)
    msg = xor(end,key)
    print(key, str(msg) + '\n')
    if "the" in str(msg):
        break

# Message is "Cooking MC's like a pound of bacon"