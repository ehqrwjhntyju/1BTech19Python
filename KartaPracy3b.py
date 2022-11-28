# # Zad 1
# for i in range(1, 31):
#   print(i)

# # Zad 2
# for i in range(1, 30):
#   if i % 2 == 1:
#     print(i**2, end=" ")

# # Zad 3
# for i in range(1000, 10000):
#   if i % 379 == 0:
#     print(i)

# # Zad 4
# for i in range(100, 1000):
#   if i % 5 and 6 or 11 == 0:
#     print(i)

# #zad 5
# n = int(input(" "))
# suma=0
# for  i in range(n):
#   k = int(input())
#   suma += k
# print(suma)

# #zad 6
# a = int(input())
# groot=0
# for i in range(2,a+1,2):
#  groot+= i
# print(a)

# #zad 7
# m = int(input())
# a=0
# for i in range(11, m+1, 2):
#   a+=i
# print(a)

# # Zad 8
L = float(input("podaj długość trwania inwestycji: "))
W0 = int(input("Podaj ile kasy wrzucasz na inwstycje: "))
W = W0
for i in range(int(L*12)):
  W = W*(1+(0.5)/100)
print(W)

# #zad 9
# n = int(input())
# suma=0
# for i in range(21,n+1,100):
#  suma+=i
# print(suma)


# # #Zad 10
# # import math
# for i in range(1, 1000):
#  if i % 10 == math.sqrt(i):
#    print(i)
#  elif i % 100 == math.sqrt(i):
#    print(i)