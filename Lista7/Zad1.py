def acronym(words):
    return "".join([x[0].upper() for x in words])

def median(numbers:list[int]):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n //2
    return (sorted_numbers[middle] + sorted_numbers[-middle]) / 2


def sqrt(x,epsilon=1e-10):

    def sqrt_recursive(x,y,epsilon):
        next_y = (y + x/y) /2
        return y if abs(next_y - y) < epsilon else sqrt_recursive(x,next_y,epsilon)
    return sqrt_recursive(x,1.0,epsilon)

def make_alpha_dict(text):
    words = text.split()
    return {char: [word for word in words if char in word] for char in (''.join(words)) if char.isalpha()}


def flatten(lst):
    return [item for sublist in lst for item in (flatten(sublist) if isinstance(sublist, (list, tuple)) else [sublist])]





if __name__ =="__main__":
    print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))
    print(median([1,1,19,2,3,4,4,5,1]))
    print(sqrt(16))
    print(make_alpha_dict("Początek i koniec, alpha i omega"))
    print(flatten([1,[[1,2],[1]],[5,[[[5,6,7,8,10]],[13]]]]))