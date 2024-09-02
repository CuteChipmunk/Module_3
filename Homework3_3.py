def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, "apple", 2.3]
value_dict = {'a': 23, 'b': "four", 'c': 1.5}

print_params(*values_list) #распаковка списка
print_params(**value_dict) #распаковка словаря

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)