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

    at_zero = dial == 0
    total = dial + n
    rotations = total // 100
    dial = total % 100
    count += abs(rotations)
    if n < 0:
        count += (dial == 0) - at_zero

    # could also use divmod() here

print(f"Final password: {count}")
