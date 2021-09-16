def pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return pow(a, b / 2) ** 2
    else:
        return a * pow(a, (b - 1) / 2) * pow(a, (b - 1) / 2)


x = float(input())
y = int(input())
print(pow(x, y))
