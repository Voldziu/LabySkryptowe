import time
from functools import lru_cache,cache
from Zad4 import make_generator,catalan,fibonacci


def make_generator_mem(f):
    @lru_cache(maxsize=None)
    def memoized_f(i):
        return f(i)
    @lru_cache(maxsize=None)
    def make_generator_memo():
        return make_generator(memoized_f)
    return make_generator_memo


 


if __name__=="__main__":
    catalan_gen = make_generator_mem(catalan)()

    fibonacci_gen = make_generator_mem(fibonacci)

    geometric_gen = make_generator(lambda n: 2 * (3 ** (n - 3)))()
    s_time = time.time()
    for i in range(30):

        print(f'Fibonacci number: {i}, {next(fibonacci_gen()())}')
    e_time = time.time()
    elapsed = e_time-s_time
    print(f'Time passed: {elapsed}')

