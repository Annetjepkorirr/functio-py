def add(a,b):
    answer = a + b
    return answer

def divide(q,r):
    answer= q/r
    return answer

def subtract(o,w):
    answer =o-w
    return answer

def multiply(s,p):
    answer =s*p
    return answer

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)