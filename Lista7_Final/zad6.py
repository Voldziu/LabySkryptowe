import logging
import functools
import time


def log(level=logging.DEBUG):
    def decorator(obj):
        if isinstance(obj, type):
            return log_class(obj, level)
        else:
            return log_function(obj, level)

    return decorator


def log_function(func, level):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time

        logger = logging.getLogger(func.__module__)
        logger.log(level,
                   f"Function {func.__name__} called with args={args}, kwargs={kwargs}, returned {result}, took {duration:.6f} seconds")

        return result

    return wrapper


def log_class(cls, level):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self._instance = cls(*args, **kwargs)
            self.logger = logging.getLogger(cls.__module__)
            self.logger.log(level, f"Class {cls.__name__} instantiated with args={args}, kwargs={kwargs}")
            self.__class__ = type(self._instance.__class__.__name__,
                                  (self.__class__, self._instance.__class__),
                                  {})
            self.__dict__ = self._instance.__dict__

    return Wrapper


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)


    @log(level=logging.ERROR)
    def add(x, y):
        return x + y


    @log(level=logging.DEBUG)
    class SampleClass:
        def __init__(self, x, **kwargs):
            self.x = x ** 2
            self.kwargs = kwargs


    result = add(3, 5)
    print("Result of example_function:", result)

    # Test the decorated class
    example_instance = SampleClass(10, jakub=10)
    print("Value of x in example_instance:", example_instance.x)
