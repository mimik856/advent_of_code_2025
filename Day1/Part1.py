def read():
    with open("FILE_NAME.txt") as f:
        return [ln.strip() for ln in f if ln.strip()]

dial = 50
count = 0

for line in read():
    direction = line[0]
    n = int(line[1:])

    if direction == "L":
        n = -n

    dial = (dial + n) % 100

    if dial == 0:
        count += 1

print(f"Final answer: {count} ({count:,})")
