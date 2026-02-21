def square(a):
  for i in range(a,-1,-1):
      yield i
a=int(input()) 


print(*square(a))



