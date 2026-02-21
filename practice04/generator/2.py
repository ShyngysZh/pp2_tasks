def power(a):
  for i in range(a+1):
    if i%2==0:
      yield i
a=int(input()) 
for i in power(a):
  if i==a-1:
    print(i)
    break
  else:
    print(i,end=",")
print() 