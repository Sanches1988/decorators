from datetime import datetime as dt

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def log(func):
    def foo(*args, **kwargs):
        date_time = dt.now()
        func_name = func.__name__
        result = func(*args, **kwargs)
        with open('logs.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата/время: {date_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {result}\n')
        return result
    return foo


@log
def generator(nested_list):
    for i in nested_list:
        for y in i:
            yield y

for item in generator(nested_list):
    print(item)