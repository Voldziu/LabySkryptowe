import random
import string


class PasswordGenerator:
    def __init__(self, length, charset, count):
        self.length = length
        self.charset = charset
        self.count = count
        self.generated_passw = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_passw < self.count:
            passwd = ''.join(random.choice(self.charset) for i in range(self.length))
            self.generated_passw += 1
            return passwd

        raise StopIteration


if __name__ == "__main__":
    charset = string.ascii_letters + string.digits + string.punctuation
    password_gen = PasswordGenerator(18, charset, 4)

    try:
        print(next(password_gen))
        print(next(password_gen))
        print(next(password_gen))
        print(next(password_gen))
        print(next(password_gen))
    except StopIteration:
        print("No next element\n")

    for passwd in PasswordGenerator(20, charset, 10):
        print(passwd)