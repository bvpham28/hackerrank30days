class Calculator():
    def power(self, n, p):
        if int(n) < 0 or int(p) < 0:
            raise Exception("n and p should be non-negative")
        return pow(n, p)
