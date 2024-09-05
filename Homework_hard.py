
def sum_all_elements(data_structure): #объявляем функцию
    sum_=0 # присваеваем начальное значение
    if isinstance(data_structure, dict): #проверяем тип, если правда, то выполняется цикл, который добавляет значение и ключ к общей сумме
        for key, value in data_structure.items():
            sum_ += sum_all_elements(key)
            sum_ += sum_all_elements(value)
    elif isinstance(data_structure, (tuple, list, set)): #снова проверка, если тип определен верно, то значения добавляются в общую сумму
        for item in data_structure:
            sum_ += sum_all_elements(item)
    elif isinstance(data_structure, (int, float)): #проверка как в предыдущих, если есть, просто добавляются к общей сумме
        sum_ += data_structure
    elif isinstance(data_structure, str): # проверка + добавление к общей сумме количество символов в строке
        sum_ += len(data_structure)
    return sum_

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = sum_all_elements(data_structure)
print(result)

