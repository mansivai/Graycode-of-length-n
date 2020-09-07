from collections import deque
import math as mt 

n = int(input())
m =int(mt.log( n , 2))
a= deque(["0","1"])
b= deque(reversed(a))
l = 1
while(l < m):
  for i in range(len(a)):
    a[i] = "0"+a[i]
  for i in range(len(b)):
    b[i] = "1"+b[i]
  l= l+1
  a = a +b
  b= deque(reversed(a))
def graycode(a):
  if(mt.log( n , 2) ==  int(mt.log( n , 2))):
    return(a)
  else:
    b2 = deque()
    c = round(n/2)
    for i in range(0 , c):
        b2.append("0" + a[i])
    if(round(n/2) == n/2):
      for j in range(0,n-c):
        b2.append("1" + a[n-c-j-1])
      return(b2)
    else:
      for j in range(0,n-c):
        b2.append("1" + a[n-c-j])
      return(b2)

arr = graycode(a)
for i in arr:
  print(i)
