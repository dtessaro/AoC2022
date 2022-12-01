#for i in open("input.csv","r"):

cal = []
f_in = "input.txt"

with open(f_in, 'r') as f:
    lines = f.readlines()
    # print(lines)

    res = 0
    for line in lines:
        if line != '\n':
            n = int(line)
            res += n
            # print(n)
            # print(res)
        else:
            cal.append(res)
            res = 0

cal.sort(reverse=True)

print(f"Step 1: {cal[0]}")
print(f"Step 2: {cal[0] + cal[1] + cal[2]}")