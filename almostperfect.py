n = int(input())
numbers = []
for i in range(1, n -1):
    if (n / i).is_integer():
        numbers.append(i)
if sum(numbers) == n:
    print(str(n) + ' is perfect')
else:
    print(str(n) + ' is not perfect')