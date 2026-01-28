x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool(False))
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

