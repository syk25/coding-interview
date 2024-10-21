def sol():
    my_list = [input() for _ in range(3)]
    idx = find_idx(my_list)
    number = find_number(my_list[idx])
    change(my_list, idx, number)
    answer = my_list[-1] + 1
    print_number(answer)


def change(my_list, idx, number):
    for i in range(idx, 3):
        my_list[i] = number
        number += 1


def find_idx(my_list):
    for i in range(len(my_list)):
        word = my_list[i]
        if word != "Fizz" and word != "Buzz" and word != "FizzBuzz":
            return i


def find_number(word):
    if word == "Fizz":
        return 3
    elif word == "Buzz":
        return 5
    elif word == "FizzBuzz":
        return 15
    else:
        return int(word)


def print_number(word):
    if word % 15 == 0:
        print("FizzBuzz")
    elif word % 5 == 0:
        print("Buzz")
    elif word % 3 == 0:
        print("Fizz")
    else:
        print(word)


sol()
