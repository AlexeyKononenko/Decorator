from datetime import datetime
import requests

def decorator(func):
    def foo(*args, **kwargs):
        date_time = datetime.now()
        func_name = func.__name__
        res = func(*args, **kwargs)
        with open('decorlog.txt', 'w', encoding='utf-8') as f:
            f.write(f'Дата/время: {date_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {res}\n')
        return res
    return foo


@decorator
def respon(*args):
    url = ' '.join(args)
    res = requests.get(url=url)
    return res.status_code

if __name__ == '__main__':
    respon('https://www.ymzmotor.ru/')