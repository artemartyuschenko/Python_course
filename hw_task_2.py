#Task 1
my_string = 'If you are learning Python or php stop it and go to learn C'
stop_words = ["Python", "php", "go", "C"]

def delete_stop_words(my_str):
    list_split = my_str.split(' ')

    for word in stop_words:
        if word in list_split:
            list_split.remove(word)
    return " ".join(list_split)

    return " ".join(filter(lambda word: word not in stop_words, list_split))


print(delete_stop_words(my_string))

#Task 2
nums_list = [2, 3, 1, 5, 8]


def divisible_number(my_list, my_num):
    return list(filter(lambda x: x % my_num == 0, my_list))


print(divisible_number(nums_list, 2))

#Task 3
def my_args(*args):
    return tuple(filter(lambda x: type(x) == str, args))


print(my_args(105, 2.0, "dafsgdgsg gfsgsgfd", 'one', 8, 'type'))

#Task 4
def lists_common(my_list_1, my_list_2):
    return list(filter(lambda x: x in my_list_2, my_list_1))


print(lists_common([5, 4, 'one', 10.0, 'one hundred'], ['two thousand', 5, 12, 10, 'one', 11, 10.0]))

#Task 5
def ladder(bricks_numbers):