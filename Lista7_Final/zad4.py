def make_generator(function):
    num = 1

    def inner_func():
        nonlocal num
        while True:
            num += 1
            yield function(num - 1)

    return inner_func


def fibonacci_of(n):
    if n in {0, 1}:
        return n

    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


seq = lambda n: 2 * n + 3

if __name__ == '__main__':
    inner_fib = make_generator(fibonacci_of)
    my_gen_fib = inner_fib()
    inner_seq = make_generator(seq)
    my_gen_seq = inner_seq()

    for i in range(20):
        print(f'Fib: {next(my_gen_fib)}')
        print(f'Seq: {next(my_gen_seq)}')
        print()