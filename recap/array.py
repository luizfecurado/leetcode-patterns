array = [10, 5, 5, 8]
mul = 1
for i in array:
    mul = mul * i

print(mul)


def mul_list(items):
    m = 1
    for i in items:
        m*=i
    return m

print(mul_list([8,5,4,6]))