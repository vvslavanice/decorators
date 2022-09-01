
'''def attach_data(func):
    func.data = 3
    return func


@attach_data
def add(x, y):
    return x + y

    ЭТО ПРИМЕР КАК РЕШАТЬ +-'''


def logger(func):
    print(func(4, 5))


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

