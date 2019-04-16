"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

Fn = Fn-1 + Fn-2
"""
def get_fibo(ind):
    if ind in [0, 1]:
        return ind
    return get_fibo(ind - 1) + get_fibo(ind - 2)

get_fibo(0)
# output: 0

get_fibo(7)
# output: 13
