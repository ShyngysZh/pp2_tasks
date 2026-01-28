fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  for i in range(1, 8):
    if i == 5:
        continue
    print(i)
    
    
    for i in range(1, 13):
    if i == 9 or i == 10:
        continue
    print(i)

  for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)
    
    for i in range(1, 11):
    if i == 7:
        continue
    print(i)



