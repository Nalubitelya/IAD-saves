def IsPointInCircle(x, y, xc, yc, r):
    if (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2:
        return "YES"
    return "NO"


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
print(IsPointInCircle(x, y, xc, yc, r))
