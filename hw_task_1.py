def length(my_str): #Task 1
    return len(my_str)

print(length("London is the capital of Great Britain"))

def lists_length_compare(my_list1, my_list2): #Task 2
    if len(my_list1) > len(my_list2):
        return len(my_list1)
    else:
        return len(my_list2)
    
print(lists_length_compare([1,2,3],[1,2,3,4,5,6,7,8]))

def add_to_list(my_list,*args): #task  3
    my_list.append(*args)
    return my_list

print(add_to_list([1,"dfdfdf",'t',1.0,1000000],"my_value"))

def more_or_less_100(my_value): #task  4
    if my_value > 100 or my_value < -100:
        print("-")
    else:
        print("+")

more_or_less_100(200)
more_or_less_100(99)

def yes_or_not(my_str_1, my_str_2): #task  5
    for i in range(len(my_str_1)):
        if my_str_1[i] != my_str_2[i]:
            break
            print('НЕТ')
    if i == (len(my_str_1)-1):
        print('ДА')
         
str_1 = 'test'
str_2 = 'test1'        
yes_or_not(str_1,str_2)