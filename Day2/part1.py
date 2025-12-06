def read():
    with open("FILE_NAME.txt", "r") as f:
        return f.readlines()[0].split(",")
    
total = 0
    
for line in read():
    start, end = map(int, line.split("-"))
    for id_num in range(start, end + 1):
        id_str = str(id_num)
        if len(id_str) % 2 != 0:
            continue
        first = id_str[:len(id_str)//2]
        second = id_str[len(id_str)//2:]
        if first == second:
            total += id_num

print(f"Final answer: {total} ({total:,})")
