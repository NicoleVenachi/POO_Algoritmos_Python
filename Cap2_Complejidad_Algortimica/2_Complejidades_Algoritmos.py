import math

class Complex:

    def  __init__(self, n):
        self.n = n

    def  o_const(self):
        return 1

    def  o_log(self):
        return math.log10(self.n)

    def  o(self):
        return self.n

    def  o_log_n(self):
        return self.n * self.o_log()

    def  o_sqr(self):
        return self.n**2

    def  o_exp(self):
        return 2**self.n

if __name__ == '__main__':
    cmpx = Complex(1000)
    print(cmpx.o_const())
    print(cmpx.o_log())
    print(cmpx.o())
    print(cmpx.o_log_n())
    print(cmpx.o_sqr())
    print(cmpx.o_exp())
