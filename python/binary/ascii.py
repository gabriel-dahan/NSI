# EX 1 :
def lower_str(text: str) -> str:
    final = ''
    for char in text:
        minc = chr(ord(char) + 32)
        if char == ' ' or 97 <= ord(char) <= 122:
            final += char
            continue
        final += minc
    return final

# EX 2 :
def is_valid(passwd: str, special_chars: bool = False) -> bool:
    valid_chars = {*range(48, 58), *range(65, 91), *range(97, 123)}
    if special_chars:
        valid_chars = {*range(33, 127)}
    for char in passwd:
        if ord(char) in valid_chars:
            continue
        return False
    return True

if __name__ == '__main__':
    print(is_valid('TheGabDooSan158.'))