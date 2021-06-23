def thought(n):
    operators = [' + ', ' - ', ' * ', ' // ']
    val = {}
    if n % 4 != 0:
        return 'no solution'
