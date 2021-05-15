import inspect


def simple_coroutine():
    print("coroutine started")
    x = yield
    print("coroutine received:", x)


def main():
    co = simple_coroutine()
    print(inspect.getgeneratorstate(co))

    next(co)
    print(inspect.getgeneratorstate(co))

    try:
        co.send(10)
    except StopIteration:
        print(inspect.getgeneratorstate(co))


if __name__ == "__main__":
    main()
