try:
  print(o)
except(NameError):
  print("Name Error Found")
try:
  a=[1,2,3,4]
  print(a[4])
except(IndexError):
  print("Index Error Found")
try:
  a={0:1,1:2}
  print(a[3])
except(KeyError):
  print("Key Error Found")
try:
  a=1
  print(a/0)
except(ZeroDivisionError):
  print("Zero Division Error Found")