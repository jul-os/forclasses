count=0
i=int(input())
while i!=0:
   next_i=int(input())
   if next_i>=i:
       count+=1
   i=next_i
print(count) 
