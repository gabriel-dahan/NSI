def dice_scores(path: str) -> int:
    import random as r
    rnb = sum(r.randint(1, 6) for _ in range(2))
    f = open(path, 'r+')
    lines = f.readlines()
    new_line = "\n" if len(lines) != 0 else ""
    f.write(f'{new_line}Score [{len(lines) + 1}] : {rnb}')
    return max([int(line.split()[-1]) for line in lines] + [rnb])

for _ in range(100):
    r = dice_scores('./scores.txt')
print(r)