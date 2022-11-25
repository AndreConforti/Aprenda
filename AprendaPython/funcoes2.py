def do_twice(f, v):
    f(v)
    f(v)


# def print_twice(bruce):
#     print(bruce)
#     print(bruce)


def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


do_four(print,'spam')
