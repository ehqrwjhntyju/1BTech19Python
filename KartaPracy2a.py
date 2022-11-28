# Zad 1
print("podaj liczbe ")
a,b = int(input()), int(input())
if (a+b) % 2 == 0:
  print("tak")
else:
  print("nie")

# Zad 2
import math
a,g = int(input()), int(input())
if (a+g)/2 > math.sqrt (a*g):
 print("tak")
else:
 print("nie")

# Zad 3

a = int(input())
b = int(input())
c = int(input())
if a==b:
   print("tak")
   print(a,b)
elif a==c:
   print("tak")
   print(a,c)
elif b==c:
   print("tak")
   print(b,c)
else:
   print("nie")

# Zad 4
a,b,c,d = int(input()), int(input()), int(input()), int(input())
print(min(a,b,c,d))

# Zad 5
a, b, c = int(input()), int(input()), int(input())
if a<(a+b) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b):
  print("tak")
else:
  print("nie")

# Zad 6 
a, b, c = int(input()), int(input()), int(input())
if a**2 + b**2 == c**2:
  print("prostokątny")
if a**2 + b**2 < c**2:
  print("rozwartokątny")
if a**2 + b**2 > c**2:
  print("ostrokątny")