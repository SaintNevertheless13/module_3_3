def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ["You will never walk alone", 1892, [3, 6, 1892]]
values_dict = {'a': [3, 6, 1892], 'b': "You will never walk alone", 'c': 1892}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [":)", 'Точка, точка, скобка']
print_params(*values_list_2, 42)