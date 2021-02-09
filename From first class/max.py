i=int(input())
max=i
count=1 #должен ли он выдавать один?
while i!=0:
   if i>max:
       max=i
       count=1
   elif i==max:
       count+=1
   i=int(input())
print(count)
