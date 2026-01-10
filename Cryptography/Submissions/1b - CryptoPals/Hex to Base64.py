import base64

hexa = ("49276d206b696c6c696e6720796f7572206"+
        "27261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

end = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

raw = bytes.fromhex(hexa); print(raw)

output = base64.b64encode(raw); print(output)