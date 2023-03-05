""" Условие задачи - https://stepik.org/lesson/701988/step/4?unit=702089 """


class Model:
    def __init__(self):
        self.fields = {}

    def query(self, **kwargs):
        self.fields.update(kwargs)

    def __str__(self):
        if not self.fields:
            return f'Model'
        return f'Model: {", ".join(" = ".join((k, str(v))) for k, v in self.fields.items())}'
