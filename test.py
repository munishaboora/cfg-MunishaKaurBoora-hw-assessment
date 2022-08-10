def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def say_hello():
    print("Hello!")


@do_twice
def say_bye():
    print("Bye!")

say_hello()
say_bye()