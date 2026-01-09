import base64

hexa = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print(hexa)
bytes = bytes.fromhex(hexa)
print(bytes)
enc_base64 = base64.b64encode(bytes)

print(enc_base64)
