count=0
i=int(input())
if i!=0:
    next_i=int(input())
    while next_i!=0:
        if next_i>i:
            count+=1
        i=next_i
        next_i=int(input())
print(count)
