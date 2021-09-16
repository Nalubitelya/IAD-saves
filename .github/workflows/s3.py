def sum(a, b):
    if b != 0:
        return sum(a + 1, b - 1)
    return a


x = int(input())
y = int(input())
print(sum(max(x, y), min(y, x)))
