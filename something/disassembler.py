import dis


def multipy(a, b):
    result = a * b
    return result


dis.dis(multipy)
