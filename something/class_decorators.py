def adv_deco(password):
    def adv_deco_inner(my_class):
        def inner(*args, **kwargs):
            if password != 'secret':
                raise ValueError('Wrong password')
            print('Success')
            return my_class(*args, **kwargs)

        return inner

    return adv_deco_inner


@adv_deco(password='secret')
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


obj = MyClass(1, 2)
