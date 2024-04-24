def forall(pred, iterable):
    return all(pred(x) for x in iterable)


def exists(pred, iterable):
    return any(pred(x) for x in iterable)


def at_least(pred, iterable, n):
    return sum(1 for x in iterable if pred(x)) >= n


def at_most(pred, iterable, n):
    return sum(1 for x in iterable if pred(x)) <= n


unary_fun = lambda x: x > 2
num_list = [1, 2, 3, 4, 5, 6, 7]

print(forall(unary_fun, num_list))
print(exists(unary_fun, num_list))
print(at_least(unary_fun, num_list, 3))
print(at_most(unary_fun, num_list, 3))