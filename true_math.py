from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second

# print(divide(68, 6))
# print(divide(23, 0))