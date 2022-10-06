def a():
    print('Star of a()')
    b()  # call b().


def b():
    print('Start of b()')
    c()  # call c().


def c():
    print('Start of c()')
    42 / 0  # This will cause a zero divide error.


a()  # Call a()
