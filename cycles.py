#For:
#1
povt = int(input("Введите кол-во повторений:"))

for i in range(povt):
    num1 = int(input("Введите число:"))
    num2 = int(input("Введите число:"))
    print(num1 + num2)

import random
#2
povt = int(input('Введите кол-во чисел:'))

s = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(povt):
    print(random.choice(s))
#3
povt = int(input("Введите кол-во повторений:"))

for i in range(povt):
    r = int(input("Введите радиус:"))
    P = 3.14

    print(P * r * r)
#While:
#1
import random
a = (random.randint(1,10000))
num = int(input('Введите число от 1 до 2:'))
if num == 1:
    while a > 0:
        print(a, end= ', ')
        a -=(random.randint(1,200))
else:
    while a > 0:
        print(a, end= ', ')
        a /=(random.randint(1,200))
#2
import random

s=int(input('Введите число:'))
h = ['Hello', 'Goodbuy', 'Hay', 'Buy']

a = 0
while a < s:
    print(random.choice(h))
    a +=(random.randint(1,5))
#3
import random

n = (random.randint(1, 9))
c = (random.randint(1, 9))

i = 0
while i < n:
    i += 1
    if i == c:
        continue
    print(i)