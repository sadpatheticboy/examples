# LEGB - local, enclosed, global, builtins

import builtins

builtins.scope = 'builtins'  # example

scope = 'global'


def outer():
    scope = 'enclosed'

    def inner():
        scope = 'local'
        print(scope)

    inner()


if __name__ == '__main__':
    outer()
