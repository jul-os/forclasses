def min_of_four(a,b,c,d):
    o=min(a,b,c,d)
    return o
a,b,c,d=map(int,input().split())
print(min_of_four(a, b, c, d))
