prev_i=int(input())
i=int(input())
count=1
while i!=0:
   if i==prev_i:
       count+=1
   prev_i=i
   i=int(input())
print(count)
