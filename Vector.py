def size_vector(x):
    return len(x)

def norma_vector(x):
    norma = 0
    for element in x:
        norma += element**2
    return (norma**(1/2))

    # norma = sum([element**2 for element in x])**0.5
    # return norma


def differ_vectors(v1, v2):
    n = len(v1)
    v = []
    for i in range(n):
        v[i] = v1[i] - v2
    return v


def skalar(x ,y):
    try:
        assert size_vector(x) == size_vector(y), f"розмірність векторів {x} та {y} різна"
        skaldob = 0
        for i in range(size_vector(x)):
            skaldob += x[i] * y[i]

        return skaldob
    except AssertionError as e:
        print(e)

def perpenducylar(x, y):
    if skalar(x, y) == 0:
        return True
    else:
        return False

def paralelnict(x, y):
    


a = [2, 2, 5]
print(norma_vector(a))
b = [1, 2]
c = [1, 0, -1]
print(skalar(a, b))
print(skalar(a, c))


if __name__ == '__main__':
    a = [2, 2, 5]
    print(norma_vector(a))
    b = [1, 2]
    c = [1, 0, -1]
    print(skalar(a, b))
    print(skalar(a, c))