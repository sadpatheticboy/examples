""" Условие задачи - https://stepik.org/lesson/701987/step/8?unit=702088 """


class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        m = request.get('method', 'GET')
        if m == 'GET':
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'
