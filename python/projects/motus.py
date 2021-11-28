def compare_words(w1: str, w2: str) -> str:
    assert len(w1) == len(w1) == 7
    if w1 == w2:
        return w1
    final = ''
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            final += w1[i].upper()
        else:
            final += w1[i].lower() if w1[i] in w2 else '.'
    return final

print(compare_words('bonjour', 'bonsoir'))