from random import randint

def encrypt_asciicypher(text: str):
    text = text.lower()
    key = ''
    for _ in range(26):
        c = chr(randint(33,127))
        while c in key:
            c = chr(randint(33,127))
        key += c
    result = ''.join(key[ord(char) - 97] for char in text)
    return key, result

key, res = encrypt_asciicypher('Sacha')
print(f'Key : {key}\nEncrypted text : {res}')