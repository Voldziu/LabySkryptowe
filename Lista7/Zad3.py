import string
import random



class PasswordGenerator:
    def __init__(self,length,charset=None,count=1):
        self.length = length
        self.charset = charset or string.ascii_letters + string.digits
        self.count = count
        self.generated_count = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.generated_count >=self.count:
            raise StopIteration
        password = ''.join(random.choices(self.charset,k=self.length))
        self.generated_count+=1
        return password



if __name__ =="__main__":
    password_gen = PasswordGenerator(length=18,count=4)
    print(next(password_gen))
    print(next(password_gen))
    print(next(password_gen))
    print(next(password_gen))

    for pswd in PasswordGenerator(20,count=10):
        print(pswd)


