from datetime import datetime as dt
import requests
FILE_PATH = 'logs.txt'

def log(path):
    def decor(func):
        def foo(*args, **kwargs):
            date_time = dt.now()
            func_name = func.__name__
            result = func(*args, **kwargs)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(f'Дата и время вызова функции: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return foo
    return decor


@log(FILE_PATH)
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://www.championat.com/football/')