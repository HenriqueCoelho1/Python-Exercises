# def add(x, y):
#     return x + y


# add(2, 3)
# result = add(2, 3)
# print(result)          # <-- this does not work

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "Your are a fool!"


result = divide(15, 0)
print(result)
