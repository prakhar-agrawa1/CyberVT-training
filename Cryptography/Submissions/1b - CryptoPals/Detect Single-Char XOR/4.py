from pwn import *
from collections import Counter

ENGLISH_FREQ = {
    'A': 0.0817, 'B': 0.0149, 'C': 0.0278, 'D': 0.0425, 'E': 0.1270,
    'F': 0.0223, 'G': 0.0202, 'H': 0.0609, 'I': 0.0697, 'J': 0.0015,
    'K': 0.0077, 'L': 0.0403, 'M': 0.0241, 'N': 0.0675, 'O': 0.0751,
    'P': 0.0193, 'Q': 0.0010, 'R': 0.0599, 'S': 0.0633, 'T': 0.0906,
    'U': 0.0276, 'V': 0.0098, 'W': 0.0236, 'X': 0.0015, 'Y': 0.0197, 'Z': 0.0007
}

def giveFreqDict(string):
    dic = {}
    for char in str(string):
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

def giveRanking(dict):
    score = 0
    for char in dict:
        if char.lower() == 'e':
            score += 11 * dict[char]
        elif char.lower() == 't':
            score += 9 * dict[char]
        elif char.lower() == 'a':
            score += 8 * dict[char]
        elif char.lower() == 'o':
            score += 7 * dict[char]
        elif char.lower() == 'i':
            score += 7 * dict[char]
        elif char.lower() == 'n':
            score += 7 * dict[char]
        elif char.lower() == 's':
            score += 6 * dict[char]
        elif char.lower() == 'h':
            score += 6 * dict[char]
        elif char.lower() == 'r':
            score += 6 * dict[char]
        elif char.lower() == 'd':
            score += 4 * dict[char]
        elif char.lower() == 'l':
            score += 4 * dict[char]
        elif char.lower() == 'u':
            score += 3 * dict[char]
        # etaoin shrdlu!!! hahhahahadhsjfhaskjhfaskhdlfj
        elif char.lower() == 'c':
            score += 3 * dict[char]
        elif char.lower() == 'm':
            score += 2 * dict[char]
        elif char.lower() == 'w':
            score += 2 * dict[char]
        elif char.lower() == 'f':
            score += 2 * dict[char]
        elif char.lower() == 'g':
            score += 2 * dict[char]
        elif char.lower() == 'y':
            score += 2 * dict[char]
        elif char.lower() == 'p':
            score += 2 * dict[char]
        elif char.lower() == 'b':
            score += 1 * dict[char]
        elif char.lower() == 'v':
            score += 1 * dict[char]
        elif char.lower() == 'k':
            score += 1 * dict[char]
        elif char.lower() == 'j':
            score += 0 * dict[char]
        elif char.lower() == 'x':
            score += 0 * dict[char]
        elif char.lower() == 'q':
            score += 0 * dict[char]
        elif char.lower() == 'z':
            score += 0 * dict[char]
    return score

def getScore(text):
    # Had to ask AI :(

    text = str(text).upper()

    letters_only = [char for char in text if char.isalpha()]
    if not letters_only:
        return float('inf')
    
    counts = Counter(letters_only)
    total_len = len(letters_only)
    score = 0

    for char, freq in ENGLISH_FREQ.items():
        obs = counts[char] / total_len
        score += ((obs-freq)**2)/freq # Chi-Squared Model

    return score

#

strings = []

with open("C:/Users/rocko/Documents/VSCode/Cyber101/Cryptography/Submissions/1b - CryptoPals/Detect Single-Char XOR/4.txt", "r") as file:
    for line in file:
        strings.append(line.split())

strings_dict = {}

for index, enc in enumerate(strings):
    for i in range(128):
        key = chr(i)
        msg = xor(enc, key)

        #freq_dic = giveFreqDict(msg) #ranking = giveRanking(freq_dic)
        
        score = getScore(msg)
        strings_dict[msg] = score


sorted_dict = dict(sorted(strings_dict.items(),key=lambda x:x[1]))

final_str = ""
for key in sorted_dict.keys():
    final_str += f'{str(sorted_dict[key])}: {key}\n'

with open("ranked_strings.txt", "w+") as file:
    file.write(final_str)
    print("success!")
