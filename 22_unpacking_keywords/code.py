# def named(**kwargs):
#     print(kwargs)


# named(name="bob", age=25)

# def named(**kwargs):
#     print(kwargs)


# details = {"Name": "Bob", "age": 25}

# named(**details)

# def named(**kwargs):
#     print(kwargs)


# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")


# print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, 4, nick="Nick", age=25)
