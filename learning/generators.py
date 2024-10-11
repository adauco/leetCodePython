import random


def create_squares(n):
    for x in range(n):
        yield x**2


def high_low_number(l, h, n):
    for i in range(n):
        yield random.randint(l,h)


def gen_fin(n):
    a = 1
    b = 1
    for x in range(n):
        yield b/a
        a,b = b, a+b


for i in high_low_number(1,10,12):
    print("random")
    print(i)

for x in gen_fin(10):
    print(x)

