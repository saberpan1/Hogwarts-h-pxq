class Calc:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return 'ERROR'
        elif a % b != 0:
            return round((a / b), 2)
        else:
            return int(a / b)
