from math import inf

def divide(first, second):
 #   division = first / second
    if second == 0:
        return inf
    else:
        return first / second
     #   print(division)
print(divide(5, 0))