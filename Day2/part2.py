def read():
    with open("FILE_NAME.txt", "r") as f:
        return f.readlines()[0].split(",")
    
total = 0
    
def is_invalid(id):
    s = str(id)
    l = len(s)

    for block in range(1, l):
        if l % block != 0:
            continue
        repeat = l // block
        if repeat < 2:
            continue
        if s == s[:block] * repeat:
            return True

    return False

for line in read():
    start, end = map(int, line.split("-"))
    for id in range(start, end + 1):
        if is_invalid(id):
            total += id

print(f"Final answer: {total} ({total:,})")
