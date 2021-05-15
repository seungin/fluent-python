import inspect
from collections import namedtuple
from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


Result = namedtuple("Result", "count average")


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def main():
    # close
    co = averager()
    print(inspect.getgeneratorstate(co))

    print(co.send(10))
    print(co.send(30))
    print(co.send(5))
    co.close()
    print(inspect.getgeneratorstate(co))

    # throw
    co = averager()
    print(inspect.getgeneratorstate(co))

    print(co.send(10))
    print(co.send(30))
    print(co.send(5))
    try:
        co.throw(ZeroDivisionError)
    except ZeroDivisionError:
        print(inspect.getgeneratorstate(co))

    # return
    co = averager()
    print(inspect.getgeneratorstate(co))

    print(co.send(10))
    print(co.send(30))
    print(co.send(5))
    try:
        co.send(None)
    except StopIteration as e:
        result = e.value
        print(result)
        print(inspect.getgeneratorstate(co))


if __name__ == "__main__":
    main()
