def bubble(a):
  n=len(list1)
  for i in range(n):
    for j in range (0,n-i-1):
      if a[j]>[j+1]:
        a[j],a[j+1]=a[j+1],a[j]

def read():
  a=eval(input('enter list of elements'))
  return a
  a=read()
  print('give originalclist =',a)
  bubble(a)
  print('after sorting the elements are =',a)
  
