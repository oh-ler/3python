#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n=int(input('введите число N'))
a=0
i=0
while n>0:
    n=n//2
    print(i)
    i=i+1
   