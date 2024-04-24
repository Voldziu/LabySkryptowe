def acronym(list_of_strings):
    return "".join([x[0].upper() for x in list_of_strings])


def median(list_of_ints):
    sorted_list = sorted(list_of_ints)
    list_length = len(sorted_list)

    return sorted_list[int((list_length - 1) / 2)] if list_length % 2 == 1 else (sorted_list[int(list_length / 2)] +
                                                                                 sorted_list[
                                                                                     int(list_length / 2 - 1)]) / 2


def sqrt(x, epsilon=1e-10):
    def sqrt_recursive(x, y, epsilon):
        next_y = (y + x / y) / 2
        return y if abs(next_y - y) < epsilon else sqrt_recursive(x, next_y, epsilon)

    return sqrt_recursive(x, 1.0, epsilon)


def make_alpha_dict(sentence):
    splited_sentence = sentence.split()

    unique_chars = set(char for word in splited_sentence for char in word if char.isalpha())
    alpha_dict = {char: [word for word in splited_sentence if char in word] for char in unique_chars}

    return alpha_dict


def flatten(lst):
    return [elem for list_ in lst for elem in (flatten(list_) if isinstance(list_, list) else [list_])]


print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))
print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))
print(make_alpha_dict("Poczatek i koniec, alpha i omega"))
print(flatten([1, [[1, 2], [1]], [5, [[[5, 6, 7, 8, 10]], [13]]]]))
print(sqrt(4))
