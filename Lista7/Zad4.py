def make_generator(f):
    def inner_generator():
        i=1
        while True:
            yield f(i)
            i+=1
    return inner_generator

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def catalan(n):
    if n == 0:
        return 1
    else:
        return catalan(n - 1) * 2 * (2 * n - 1) // (n + 1)




if __name__ =="__main__":
    catalan_gen = make_generator(catalan)()
    fibonacci_gen = make_generator(fibonacci)()

    geometric_gen = make_generator(lambda n: 2*(3**(n-3)))()

    for i in range(100):
        print(f'Fibonacci number: {i}, {next(fibonacci_gen)}')



