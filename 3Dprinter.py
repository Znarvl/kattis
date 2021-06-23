def printer(n):
    printer = 1
    days = 0
    while printer < n:
        printer = printer * 2
        days += 1
    days += 1
    return days

print(printer(int(input())))