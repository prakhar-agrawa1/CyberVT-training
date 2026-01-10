from pwn import *

def repeatXOR(msg, key):
    enc = ""
    for i in range(len(msg)):
        msg_ch = msg[i]
        key_ch = key[i%len(key)]
        new_ch = bytes.hex(xor(msg_ch, key_ch))
        enc += str(new_ch)
    return enc

msg = '''Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal'''
key = 'ICE'

print(repeatXOR(msg, key))

pswd = "password1234"
key = "PASSWORD5678"

print(repeatXOR(pswd,key))

email = "Hi Mr. C, I hope...Respectfully, P"
key = "password"

print(email)
enc_email = repeatXOR(email,key)
print(enc_email)
print(bytes.fromhex(repeatXOR(bytes.fromhex(enc_email), key)))