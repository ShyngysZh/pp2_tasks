def power(a):
  for i in range(a+1):
    yield i**2
a=int(input()) 
for i in power(a):
  print(i,end=" ")
print() 