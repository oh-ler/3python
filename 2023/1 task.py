N = int(input('Введите количество монет '))
o = r = 0
for i in range(N):
    x = int(input('Введи 1, если орел, иначе 0:'))
    if x == 1:
        o += 1
    else:
        r += 1
if o < r:
    print(f'Переверните {o} монет с орла на решку')
elif o == r:
    print((f'Количество орлов и решек одинаково, по {o} штук'))
else :
    print((f'Переверните {r} монет с решки на орла'))

