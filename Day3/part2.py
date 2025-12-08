def read():
    with open("FILE_NAME.txt", "r") as f:
        return [ln.strip() for ln in f if ln.strip()]
    
total = 0

for bank in read():
    needed = 12
    remove = len(bank) - 12
    stack = []

    for digit in bank:
        d = int(digit)

        while stack and remove > 0 and stack[-1] < d:
            stack.pop()
            remove -= 1

        stack.append(d)

    if remove > 0:
        stack = stack[:-remove]

    chosen = stack[:12]

    total += int("".join(map(str, chosen)))
    
print(f"Final answer: {total} ({total:,})")
