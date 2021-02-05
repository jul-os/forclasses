a, b, c, d = map(int, input().split())
for i in range(1001):
    if a*(i**7)+b*(i**2)+c*i+d==0:
        print(i)