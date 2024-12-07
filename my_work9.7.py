def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for i in range(2, res):
            if (res % i) == 0:
                print('Составное')
                break
        else:
            print('Простое')
        return res
    return wrapper

@is_prime
def sum_three(*args):
    s = sum(args)
    return s


result = sum_three(2, 3, 6, 9)

print(result)