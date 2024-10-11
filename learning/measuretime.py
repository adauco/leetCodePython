import time
import timeit

def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str,range(n)))

def test():
    start = time.time()
    func_one(10000)
    end = time.time()
    print(end - start)

    start = time.time()
    func_two(10000)
    end = time.time()
    print(end - start)


stmt = '''func_one(100)'''
setup = '''def func_one(n):
    return [str(num) for num in range(n)]'''
print(timeit.timeit(stmt, setup, number=10000))

stmt = '''func_two(100)'''
setup = '''def func_two(n):
    return list(map(str,range(n)))'''
print(timeit.timeit(stmt, setup, number=10000))
