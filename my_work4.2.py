def test_function(x):
    d = x ** 2
    def inner_function():
        print('"Я в области видимости функции test_function"')
    inner_function()
    return d


x = 5

print(test_function(x))

inner_function()