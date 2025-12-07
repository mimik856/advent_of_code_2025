def read():
    with open("FILE_NAME.txt", "r") as f:
        return [ln.strip() for ln in f if ln.strip()]
    
total = 0

for bank in read():
    best = 0
    for i in range(len(bank)):
        a = int(bank[i])
        for j in range(i + 1, len(bank)):
            b = int(bank[j])
            val = a * 10 + b
            if val > best:
                best = val
    total += best
    

print(f"Final answer: {total} ({total:,})")
