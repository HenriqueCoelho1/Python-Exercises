default_y = 5


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)

# this does not work
default_y = 4
add(2)
