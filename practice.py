import math
def is_triangle(a, b, c):
    s = a+b+c
    Area = math.sqrt(s*((s-a)+(s-b)+(s-c)))

    return False if Area > 0 else True


print(is_triangle(2,2,4))