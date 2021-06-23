n = int(input())
for y in range(n):
    t = int(input())
    pos = input().split()
    posList = [int(x) for x in pos]
    distance = max(posList) - min(posList)
    answer = distance * 2
    print(answer)


