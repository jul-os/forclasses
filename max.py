i=int(input())
max=i
count=0
while i!=0:
   next_i=int(input())
   if next_i>i:
       max=next_i
       count=1
       continue
   if next_i==max:
       count+=1
   i=next_i
print(count)