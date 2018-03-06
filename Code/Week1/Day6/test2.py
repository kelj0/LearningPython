def foo():
    try:
        return 42/0
    except ZeroDivisionError:
        print('a')

print(foo())