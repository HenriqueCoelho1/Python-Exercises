# def add(x, y):
#     return x + y

# add = lambda x, y: x + y
# def add(x, y): return x + y


# print(add(5, 7))

def double(x):
    return x * 2


sequence = [1, 3, 5, 7]
doubled = [double(x) for x in sequence]
# both are the same thing
doubled = map(double, sequence)
