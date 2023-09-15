n=int(input("enter value: "))
m=m[n]*0
for i in range(1,n+1):
 for k in range(i,n+1):
  if k%i==0:
   if(m[k]==0):
    m[k]=1
   else:
    m[k]=0
for i in range(1,n+1)
 if m[k]==1:
  print(i,end=",")
  