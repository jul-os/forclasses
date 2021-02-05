i=int(input())
max=i
count=0
next_i=int(input())
while next_i!=0:
   if next_i>i:
       max=next_i
       count=1
   elif next_i==max:
       count+=1
   next_i=i
   next_i=int(input())
print(count)
