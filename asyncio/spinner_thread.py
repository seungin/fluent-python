import threading
import itertools
import time


def spin(msg, done):
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg
        print(status, flush=True, end="\r")
        if done.wait(0.1):
            break
    print(" " * len(status), end="\r")


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    done = threading.Event()
    spinner = threading.Thread(target=spin, args=("thinking!", done))
    print("spinner object:", spinner)
    spinner.start()
    result = slow_function()
    done.set()
    spinner.join()
    return result


def main():
    result = supervisor()
    print("Answer: ", result)


if __name__ == "__main__":
    main()
