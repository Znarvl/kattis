n = input().split(';')
tot = 0
for i in n:
    if '-' in i:
        split = i.split('-')
        for j in range(int(split[0]), int(split[1]) + 1):
            tot += 1
    else:
        tot += 1
print(tot)
